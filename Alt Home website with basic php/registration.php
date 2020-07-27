<?php
$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$gender = $_POST['gender'];
$empid = $_POST['empid'];
$email = $_POST['email'];
$pass = $_POST['pass'];

//database connection

$conn = new mysqli('localhost','root','','medbot');
if($conn->connect_error)
{
    die('Connection Failed : '.$conn->connect_error);
}
else
{
    $stmt = $conn->prepare("insert into registration(firstname, lastname, gender, empid, email, pass) values(?,?,?,?,?,?)");
    $stmt->bind_param("ssssss", $firstname, $lastname, $gender, $empid, $email, $pass);
    $stmt->execute();
    header("Location:http://localhost/registration/login.html");
    $stmt->close();
    $conn->close();

}
?>
