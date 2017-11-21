<?php
	//going to insert from settings page
	//connection is $mysqli 
	include('config.php');
	
	//mysqli for security reasons, aka SQL Injection
	$userName = mysqli_real_escape_string($mysqli,$_POST['username'])
	$userEmail = mysqli_real_escape_string($mysqli,$_POST['email'])
	$password = mysqli_real_escape_string($mysqli,$_POST['pswd'])
		
	//query, insert // ask allison about additional preference headings
	$query = "INSERT INTO Preference (name, userEmail, password ) VALUES 
		('$userName','$userEmail', '$password' );"
		
	if (!mysqli_query($mysqli,$query))
	{
		die('Error: ' . mysqli_error($mysqli));
	}
	echo "1 record added "
	
	mysqli_close($mysqli);
	//try to get saveAndExit unless Allison got that completed
?>
	
	
   
   