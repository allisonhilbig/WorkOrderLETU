$(document).ready(function(){
    $("*").submit(function checkCredentials() {
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
            alert();
            action="http://cs-lab.letu.edu/~sw2proj/MainMenu.html"
        }
    });
});

$(document).ready(function(){
    $("#signupbtn").on('click', function(e){
        e.preventDefault();
        $.ajax({method: "POST",
                url: "login.php",
                data: { "id": $("#login").val(), 
                        "uname": $("#username").val(),
                        "pword": $("#pswd").val()}
        }).done(function(data){
            var result = $.parseJSON(data);
          
            if(result==1){
                str='Please check email account for confirmation email.';
            } else if(result==2) {
                str='All fields are required.';
            } else {
                str='Error: Please try again.';
            }

            alert(str);
        });      
    });
});