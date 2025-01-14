from flask import Blueprint, redirect
from flask import render_template, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from .form import Login, ClientSigninForm, RiderSigninForm, LocalSigninForm
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash,check_password_hash
from . import cliente, rider, negozio
from .models import Cliente, Rider, Local  # NON LO CANCELLARE; Missing user_loader or request_loader
from . import login

auth = Blueprint('auth', __name__)


@login.user_loader
def load_user(Email):
    u = cliente.find_one({"Email": Email})
    if u:
        return Cliente(Email=u['Email'], type=0)
    else:
        u = rider.find_one({"Email": Email})
        if u:
            return Rider(Email=u['Email'],  type=1)
        else:
            u = negozio.find_one({"Email": Email})
            if u:
                return Local(Email=u['Email'],  type=2)
            else:
                return None



@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.customerindex'))
    form = Login()

    formemail = form.email.data
    formpassword = form.password.data

    if form.validate_on_submit():
        user = cliente.find_one({"Email": formemail})
        if user:
            if check_password_hash(user["Password"], formpassword):
                flash("Accesso Eseguito")
                user_obj = Cliente(Email=user['Email'], type=0)
                login_user(user_obj, True)
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('views.customerindex')
                return redirect(next_page)
            else:
                flash("Password Errata", category='error')
        if not user:
            user = rider.find_one({"Email": formemail})
            if user:
                if check_password_hash(user["Password"], formpassword):
                    flash("Accesso Eseguito")
                    user_obj = Rider(Email=user['Email'], type=1)
                    login_user(user_obj, True)
                    next_page = request.args.get('next')
                    if not next_page or url_parse(next_page).netloc != '':
                        next_page = url_for('views.riderindex')
                    return redirect(next_page)
                else:
                    flash("Password Errata", category='error')
        if not user:
            user = negozio.find_one({"Email": formemail})
            if user:
                if check_password_hash(user["Password"], formpassword):
                    flash("Accesso Eseguito")
                    user_obj = Local(Email=user['Email'], type=2)
                    login_user(user_obj, True)
                    next_page = request.args.get('next')
                    if not next_page or url_parse(next_page).netloc != '':
                        next_page = url_for('views.localindex')
                    return redirect(next_page)
                else:
                    flash("Password Errata", category='error')
            else:
                flash("Email non registrata", category='error')

    return render_template('login.html', form = form)



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Sei stato disconnesso.')
    return redirect(url_for('views.index'))


@auth.route("/signin", methods=['GET', 'POST'])
def signin():

    form = ClientSigninForm()

    if request.method == 'POST':

        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')

        user = cliente.find_one({"Email": form.email.data})

        if user is None:
            if len(email) < 3:
                flash("L'email deve essere di almeno 4 caratteri!", category="error")
            elif len(name) < 3:
                flash("Il nome deve essere di almeno 3 caratteri!", category="error")
            elif len(password) < 7:
                flash("La password deve essere di almeno 7 caratteri!", category="error")
            else:
                flash('Account creato!', category="success")

                account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                           "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode,
                           "Email": email, "Password": password}
                cliente.insert_one(account)
                return redirect(url_for('views.index'))
        else:
            flash("Email già registrata", category="error")

    return render_template('signin.html' , form=form)



@auth.route("/signinrider", methods=['GET', 'POST'])
def signinrider():

    form = RiderSigninForm()

    if request.method == 'POST':

        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')
        id = form.id.data
        iban = form.iban.data

        user = rider.find_one({"Email": form.email.data})

        if user is None:
            if len(email) < 3:
                flash("L'email deve essere di almeno 4 caratteri!", category="error")
            elif len(name) < 3:
                flash("Il nome deve essere di almeno 3 caratteri!", category="error")
            elif len(password) < 7:
                flash("La password deve essere di almeno 7 caratteri!", category="error")
            else:
                flash('Account creato!', category="success")

                account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                           "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode,
                           "Email": email, "Password": password, "ID": id, "IBAN" : iban}
                rider.insert_one(account)
                return redirect(url_for('views.index'))
        else:
            flash("Email già registrata", category="error")

    return render_template('signinrider.html' , form=form)


@auth.route("/signinlocal", methods=['GET', 'POST'])
def signinlocal():

    form = LocalSigninForm()

    if request.method == 'POST':

        name = form.name.data
        surname = form.surname.data
        street = form.street.data
        city = form.city.data
        province = form.province.data
        date = form.date.data
        gender = form.gender.data
        telephone = form.telephone.data
        taxcode = form.taxcode.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method='sha256')
        id = form.id.data
        iban = form.iban.data
        localname = form.localname.data
        piva = form.piva.data

        user = negozio.find_one({"Email": form.email.data})

        if user is None:
            if len(email) < 3:
                flash("L'email deve essere di almeno 4 caratteri!", category="error")
            elif len(name) < 3:
                flash("Il nome deve essere di almeno 3 caratteri!", category="error")
            elif len(password) < 7:
                flash("La password deve essere di almeno 7 caratteri!", category="error")
            else:
                flash('Account creato!', category="success")

                account = {"Name": name, "Surname": surname, "Street": street, "City": city, "Province": province,
                           "Birthday": date, "Gender": gender, "PhoneNumber": telephone, "TaxCode": taxcode,
                           "Email": email, "Password": password, "ID": id, "IBAN" : iban, "LocalName": localname, "IVA": piva}
                negozio.insert_one(account)
                return redirect(url_for('views.index'))
        else:
            flash("Email già registrata", category="error")

    return render_template('signinlocal.html' , form=form)