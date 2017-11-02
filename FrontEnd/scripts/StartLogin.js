$("button").click(function checkCredentials() {
    var uname = $(this).attr('username');
    var pword = $(this).attr('pswd');

    var credentialsCorrect = false;
    var credentialsVerified = false;

    var request = $.ajax({
        login: uname,
        password: pword
    })

    //Check if credentials are in the db
    //Check if credentials are verified
    
    if(!credentialsCorrect) {
        alert("Incorrect log in, please try again");
        document.startLogin.username.value = '';
        document.startLogin.pswd.value = '';
    }
    else if (!credentialsVerified) {
        alert("Please verify your email before continuing");
    }
    else {
        window.location.replace("http://www.google.com");
    }
});

