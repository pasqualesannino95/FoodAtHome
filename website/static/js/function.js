

function signinLocalControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var documento = document.getElementById("Document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
    var iban = document.getElementById("Iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
    var iva = document.getElementById("Iva").value
    if(iva == "")
        alert(" il campo 'Partita IVA' è vuoto")
    var locale = document.getElementById("LocalName").value
    if(locale == "")
        alert(" il campo 'Nome del locale' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}

function signinClientControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value;
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}

function signinRiderControl() {
    var nome = document.getElementById("Name").value
    if(nome == "")
        alert(" il campo 'Nome' è vuoto")
    var cognome = document.getElementById("Surname").value;
    if(cognome == "")
        alert(" il campo 'Cognome' è vuoto")
    var indirizzo = document.getElementById("Address").value
    if(indirizzo == "")
        alert(" il campo 'Indirizzo' è vuoto")
    var data = document.getElementById("Date").value
    if(data == "")
        alert(" il campo 'Data' è vuoto ")
    var telefono = document.getElementById("Telephone").value
    if(telefono == "")
        alert(" il campo 'Numero di cellulare' è vuoto")
    var fiscale = document.getElementById("Taxcode").value
    if(fiscale == "")
        alert(" il campo 'Codice fiscale' è vuoto")
    var documento = document.getElementById("Document").value
    if(documento == "")
        alert(" il campo 'Documento' è vuoto")
    var iban = document.getElementById("Iban").value
    if(iban == "")
        alert(" il campo 'IBAN' è vuoto")
    var email = document.getElementById("Email").value
    if(email == "")
        alert(" il campo 'Email' è vuoto")
    var password = document.getElementById("Password").value
    if(password == "")
        alert(" il campo 'Password' è vuoto")
}


function upperCase() {
    const f = document.getElementById("Taxcode");
    f.value = f.value.toUpperCase();
    const d = document.getElementById("Document");
    d.value = d.value.toUpperCase();
    const ib = document.getElementById("Iban");
    ib.value = ib.value.toUpperCase();
    const iv = document.getElementById("Iva");
    iv.value = iv.value.toUpperCase();
}


function viewNewOrder() {
    var div = document.getElementById("NewOrder");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}


function viewMenuControl() {
    var div_menu = document.getElementById("MenuControl");
    var div_order = document.getElementById("OrderControl");
    if (div_menu.style.display === "none") {
        div_menu.style.display = "block";
        div_order.style.display = "none";
    } else {
        div_menu.style.display = "none";
    }
}
function viewOrderControl() {
    var div_menu = document.getElementById("MenuControl");
    var div_order = document.getElementById("OrderControl");
    if (div_order.style.display === "none") {
        div_order.style.display = "block";
        div_menu.style.display = "none";
    } else {
        div_order.style.display = "none";
    }
}


function viewInsertProduct() {
    var div_ins = document.getElementById("InsertProduct");
    var div_rem = document.getElementById("RemoveProduct");
    var div_mod = document.getElementById("ModifyProduct");
    if (div_ins.style.display === "none") {
        div_ins.style.display = "block";
        div_rem.style.display = "none";
        div_mod.style.display = "none";
    } else {
        div_ins.style.display = "none";
    }
}
function viewModifyProduct() {
    var div_ins = document.getElementById("InsertProduct");
    var div_rem = document.getElementById("RemoveProduct");
    var div_mod = document.getElementById("ModifyProduct");
    if (div_mod.style.display === "none") {
        div_mod.style.display = "block";
        div_ins.style.display = "none";
        div_rem.style.display = "none";
    } else {
        div_mod.style.display = "none";
    }
}
function viewRemoveProduct() {
    var div_ins = document.getElementById("InsertProduct");
    var div_rem = document.getElementById("RemoveProduct");
    var div_mod = document.getElementById("ModifyProduct");
    if (div_rem.style.display === "none") {
        div_rem.style.display = "block";
        div_ins.style.display = "none";
        div_mod.style.display = "none";
    } else {
        div_rem.style.display = "none";
    }
}


function viewShiftPage(){
    var div_shi = document.getElementById("ShiftPage");
    var div_ord = document.getElementById("OrderPage");
    if (div_shi.style.display === "none") {
        div_shi.style.display = "block";
        div_ord.style.display = "none";
    } else {
        div_shi.style.display = "none";
    }
}
function viewOrderPage(){
    var div_shi = document.getElementById("ShiftPage");
    var div_ord = document.getElementById("OrderPage");
    if (div_ord.style.display === "none") {
        div_ord.style.display = "block";
        div_shi.style.display = "none";
    } else {
        div_ord.style.display = "none";
    }
}