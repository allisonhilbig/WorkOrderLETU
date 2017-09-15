function checkCredentials() {
    var uname = document.startLogin.username.value;
    var pword = document.startLogin.pswd.value;

    var credentialsCorrect = false;

    

    if(!credentialsCorrect) {
        alert("Incorrect log in, please try again");
        document.startLogin.username.value = '';
        document.startLogin.pswd.value = '';
    }
    else {
        window.location = 'http://wol.letu.edu/newurl';
    }

}