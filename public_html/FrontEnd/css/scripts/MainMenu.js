

function createWorkOrder() {
    window.location.replace("cs-lab.letu.edu/~sw2proj/WorkOrder1.html");
}

function changeSettings() {
    window.location.href = 'cs-lab.letu.edu/~sw2proj/SettingsPage.html';
}

function logOff() {
    //end user session
    window.location.href = 'cs-lab.letu.edu/~sw2proj/StartLogin.html';
}

function loadUser() {
    document.getElementById("usernameLabel").innerHTML = "TEST!";
    //document.StartLogin.username.value;
}