<?php

        session_start();
        require_once("db-con.php");
       
    if (isset($_POST['lsubmit'])) {
         $user_email =  $_POST['email'];
        $user_pwd = $_POST['user_pwd'];
 
        
            if (empty($user_email) || empty(($user_pwd))) {
              
                    header("Location:signin.php?login=empty");
                    
                        exit();
            } else {
                    $query = "SELECT * FROM users WHERE Email = '$user_email'";
                    $mysqli_result = mysqli_query($conn, $query); 
                        if(mysqli_num_rows($mysqli_result) < 1) {
                             header("Location: signin.php?login=wrong_email");
                            
                                exit();
                        } else {
                             $row = mysqli_fetch_assoc($mysqli_result);
                             
                             $hashed_pwd_check = password_verify($user_pwd, $row['password']);
                             if ($hashed_pwd_check === false) {
                                header("Location:signin.php?login=wrong_pwd");
                                  
                             } else if ($hashed_pwd_check === true && $row['usertype']=='user' && $row['status']=='verified' ) {  //log in the user
                                  $_SESSION["loggedin"] = true;
                                  $_SESSION["id"] = $id;
                                 $_SESSION['username'] = $row['username'];
                                 $_SESSION['email'] = $row['Email'];
                                 $_SESSION['FName'] = $row['FName'];
                                 $_SESSION['LName'] = $row['LName'];


                                    header("Location:home.php?login=login_successful");
                                    exit();
                             }

                             

                             else{
                                header("Location:signin.php?login=error");
                             }

                        }
            
    } 
  }