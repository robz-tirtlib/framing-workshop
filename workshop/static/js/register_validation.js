function validateForm() {
    var formData = new FormData(document.querySelector('form'));
    if (!validatePasswords(formData) || !validateEmail(formData)) {
        event.preventDefault();
    }
}

function validatePasswords(formData) {
    var password = formData.get("password");
    var password2 = formData.get("password2");

    if (password == "" || password2 == "") {
        alert("Пароли не должны быть пустыми");
        return false;
    } else if (password != password2) {
        alert("Пароли должны совпадать.");
        return false;
    }
    return true;
}

function validateEmail(formData) {
    var email = formData.get("email");
    var re = /\S+@\S+\.\S+/;
    if (!re.test(email)) {
        alert("Несуществующий e-mail.");
        return false;
    }
    return true;
}