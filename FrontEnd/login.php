<?php
	include("config.php")
	session_start();
//Step1
 if($_SERVER["REQUEST_METHOD"] == "POST")
 {
	$uname = mysqli_real_escape_string($mysqli,$_POST['uname'];
	$pword = mysqli_real_escape_string($mysqli,$_POST['pword'];
 
//Step2
$sql = "SELECT idPreference FROM Preference WHERE name = '$uname' and password = $'pword'";

$result = mysqli_query($db,$sql);
$row = mysqli_fetch_array($result,MYSQLI_ASSOC);
$count = mysqli_num_rows($result);

if($count == 1)
	{
	session_register("uname");
	$_SESSION['login_user'] = $uname;
	
	header("location: mainMenu.php");
	}
	else 
	{
		$error = "Invalid Login Name or Password";
		
	}
	
}

?>