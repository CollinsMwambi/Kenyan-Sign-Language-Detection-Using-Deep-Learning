<?php
require_once('db-con.php');


if(isset($_GET['code'])){

    $code=$_GET['code'];
    
    $mysqli= NEW MySQLi('localhost','root','','adbc');

$resultSet = $mysqli->query("SELECT status,code FROM users WHERE status='notverified' AND code='$code' ");

if($resultSet->num_rows == 1){

    $update= $mysqli->query("UPDATE  users SET status='verified' WHERE code='$code' ");

    if($update){

        header("Location: login.php?Your_account_has_been_verified_You_can_now_login");
       
    }else{
        echo"database error";
    }
}else{

    echo"Invalid";
}
}else{
    die("Something went wrong");
}


?>