<?php
session_start();
    require_once('db-con.php');
    if (isset($_POST['ssubmit'])) {
        
        $FName =  $_POST['FName'];
        $LName =  $_POST['LName'];
        $Email =  $_POST['Email'];
         $username = $_POST['username'];
         $user_pwd =  $_POST['user_pwd'];
          $CPassword =  $_POST['CPassword'];

          


      

            if (empty($FName) || empty($LName) || empty($Email) || empty($username) ||empty($user_pwd) || empty($CPassword)) {
                    header("Location:registration.php?signup=empty_fields");
                        exit();
            } else if (!preg_match("/^[a-zA-Z]*$/", $FName) || !preg_match("/^[a-zA-Z]*$/", $LName) ) {
                    header("Location:registration.php?signup=invalidnames");
                        exit();

                    } elseif ($user_pwd!= $CPassword) {
                      header("location:registration.php?error=passwords_dont_match");
                          exit();


            } else if (!filter_var($Email, FILTER_VALIDATE_EMAIL)) {
                     header("Location:registration.php?signup=invalid_email");
                        exit();
            } else {
                    $check_user_existence = "SELECT * FROM users WHERE username = '{$username}'";
                    $check_user_result = mysqli_query($conn, $check_user_existence);
                        if (mysqli_num_rows($check_user_result) > 0) {
                              header("Location: registration.php?signup=user_taken");
                                exit();   
                        } else {
                             $hashed_pwd = password_hash($CPassword, PASSWORD_DEFAULT);
                             $code =md5(time().$FName);
                           $status="notverified";
                           
                             $sql = "INSERT INTO users(FName,LName,Email,username,password,code,status) VALUES('$FName','$LName','$Email','$username','$hashed_pwd','$code','$status')";
                             $datacheck = mysqli_query($conn, $sql);          
        if($datacheck){
            $receiver=$Email;
            $subject = "Eshara Email Verification Link";
            $message = "<a href ='http://localhost/IsProject/verify.php?code=$code'>Register your Account by clicking this link</a>";
            $senders = "From: afma.a@yahoo.com \r\n";
            $senders .= "MIME-Version: 1.0" . "\r\n";
            $senders .= "Content-type:text/html;charset=UTF-8" . "\r\n";
        
            

            mail($receiver,$subject,$message,$senders);
            header('location:verfication.php');
            
            }else{
              header("Location:registration.php?error signing in");
            }
        }
    }

}
                             ?>