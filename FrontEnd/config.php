<?php
//Step1

$host = 'localhost';
$username = 'sw2proj';
$password = 'password';
$dbname = 'sw2projdb';
$mysqli = mysqli_connect($host, $username, $password, $dbname); 


if ($mysqli->connect_error)
	{
		die("Connection to database failed: " . $mysqli->connect_error);
	}	
//just to ensure connection :)
$query = "SELECT userEmail FROM Preference WHERE name = 'annjones'";
$result = $mysqli->query($query);

$row = mysqli_fetch_array($result);

$str = implode(" ",$row);
echo $str;
	
	
 
?>