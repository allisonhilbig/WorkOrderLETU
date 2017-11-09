<?php
	//going to insert from settings page
	//connection is $mysqli 
	include('config.php');
	
	//mysqli for security reasons, aka SQL Injection
	$userEmail = mysqli_real_escape_string($mysqli,$_POST['userEmail'])
	$roomNumber = mysqli_real_escape_string($mysqli,$_POST['roomNumber'])
	$raName = mysqli_real_escape_string($mysqli,$_POST['raName'])
	$raEmail = mysqli_real_escape_string($mysqli,$_POST['raEmail'])
	$rdEmail = mysqli_real_escape_string($mysqli,$_POST['rdEmail'])
	
	//query, insert // ask allison about additional preference headings
	$query = "INSERT INTO Preference (userEmail, raEmail, rdEmail, rdEmail, roomNumber ) VALUES 
		('$userEmail','$raEmail', '$rdEmail', $roomNumber' )";
		
	if (!mysqli_query($mysqli,$query))
	{
		die('Error: ' . mysqli_error($mysqli));
	}
	echo "1 record added "
	
	mysqli_close($mysqli);
	//try to get saveAndExit unless Allison got that completed
?>
	
	
   
   