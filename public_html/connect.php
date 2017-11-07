<?php
//Step1
 $mysqli = mysqli_connect('localhost','sw2proj','password','sw2projdb')
 or die('Error connecting to MySQL server.');
?>

<html>
 <head>
 <  /head>
 <body>
 <h1>PHP connect to MySQL</h1>

<?php
//Step2
$query = "SELECT userEmail FROM Preference WHERE name = 'annjones'";
$result = $mysqli->query($query);
$row = $result->fetch_array(MYSQLI_NUM);
printf ("%s (%s)\n", $row[0]);

$row = mysqli_fetch_array($result);

$str = implode(" ",$row);
echo $str;

?>

</body>
</html>