function createAccount() {
    var uname = document.createUser.username.value;
    var email = document.createUser.email.value;
    var pword = document.createUser.pswd.value;
    var pword1 = document.createUser.pswd1.value;

    if(pword == pword1) {
        //Store user account
        alert("Please confirm your email using the email sent to you now.");
        window.location.href = 'cs-lab.letu.edu/~sw2proj/StartLogin.html';
    }
    else {
        alert("Passwords must match");
    }
}
