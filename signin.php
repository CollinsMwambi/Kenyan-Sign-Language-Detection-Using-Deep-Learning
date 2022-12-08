<?php
// Initialize the session
session_start();

?>
<html>
<head>
  <title>Login</title>
  
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

  <link rel="stylesheet" type="text/css" href="authentication.css">
</head>
<body>
<div class="container d-flex justify-content-center align-items-center"

style="min-height:100vh; "
>
  
<form class="border shadow p-3 rounded"
action="checklogin.php"
method="post" 


style="width:450px; ">
<h1 class="text-center p-3">Login</h1>
<?php
$fullUrl="http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
if(strpos($fullUrl,"login=empty")==true){
echo"<p style=background-color:red;>Fill in all fields!!<p>";

}

elseif(strpos($fullUrl,"login=wrong_email")==true){
  echo"<p style=background-color:red;>user does not exist!!<p>";

  }
  elseif(strpos($fullUrl,"login=wrong_pwd")==true){
    echo"<p style=background-color:red;>You have entered the wrong password!!<p>";
 
    }

    elseif(strpos($fullUrl,"login=error")==true){
      echo"<p style=background-color:orange;>Error logging in,Email is not verified<p>";
   
      }

      elseif(strpos($fullUrl,"New_record_created_successfully")==true){
        echo"<p style=background-color:green;>Registration was successful, You can now log in<p>";
     
        }

        elseif(strpos($fullUrl,"Your_account_has_been_verified_You_can_now_login")==true){
          echo"<p style=background-color:green;>Account Verification was successful, You can now log in<p>";
       
          }

          elseif(strpos($fullUrl,"sreset")==true){
            echo"<p style=background-color:green;You can now login with your new password<p>";
         
            }
?>
<?php
$fullUrl="http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
if(strpos($fullUrl,"sreset")==true){
echo"<p style=background-color:green;>You can now log in with your new password<p>";

}

?>
  
  <div class="mb-3">
    <label for="Email"
     class="form-label">Email</label>
    <input type="email"
     class="form-control"
     name="email" 
     
     >
     
  
  </div>
  <div class="mb-3">
    <label for="Password"
     class="form-label">Password</label>
    <input type="Password"
     class="form-control"
     name="user_pwd" 
     >
     
    
  </div>

  
  
  <button type="submit" name="lsubmit" class="btn btn-dark">Login</button>
  <a href="Registration.php" style="text-decoration:none; ">  New here? Sign up</a>
<div>
  <a href="reset.php" style="text-decoration:none;">  forgot password?</a></div>
 
</form>


</div>

</body>
</html>