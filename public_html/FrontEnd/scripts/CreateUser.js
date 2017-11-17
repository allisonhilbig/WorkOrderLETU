$(document).ready(function(){
    $("#signupbtn").on('click', function(e){
        e.preventDefault();
        $.ajax({method: "POST",
                url: "../php/createUser.php",
                data: { id: $("#createAccount").val(), 
                        username: $("#username").val(),
                        email: $("#email").val(),
                        password: $("#pswd").val()} 
    }).done(function(data){
            var result = $.parseJSON(data);
            var str = '';
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