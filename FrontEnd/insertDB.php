<?php
//Step1
 $mysqli = mysqli_connect('localhost','sw2proj','password','sw2projdb')
 or die('Error connecting to MySQL server.');

//Get data from client side, uname, pword
//Step2
$uname = $_POST['uname'];
$pword = $_POST['pword'];

$query = "SELECT userEmail FROM Preference WHERE name = 'annjones'";
$result = $mysqli->query($query);

$row = mysqli_fetch_array($result);

$str = implode(" ",$row);
echo $str;

/* If results from database push to result array */
if ($result->num_rows > 0)
{
    while($row = $result->fetch_assoc())
    {
       array_push($result, $row);
    }
}

/*send JSON encoded array */
echo json_encode($result);

$mysqli->close();

?>