<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.87.0">
    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.104.2">
   
    <link rel="canonical" href="https://getbootstrap.com/docs/5.2/examples/heroes/">

    

    

<link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">


    <link rel="canonical" href="https://getbootstrap.com/docs/5.2/examples/heroes/">

    

    

<link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <title>Eshara</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/5.1/examples/carousel/">

    <link rel="stylesheet" type="text/css" href="welcome.css">

    <!-- Bootstrap core CSS -->
<link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      .b-example-divider {
        height: 3rem;
        background-color: rgba(0, 0, 0, .1);
        border: solid rgba(0, 0, 0, .15);
        border-width: 1px 0;
        box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
      }

      .b-example-vr {
        flex-shrink: 0;
        width: 1.5rem;
        height: 100vh;
      }

      .bi {
        vertical-align: -.125em;
        fill: currentColor;
      }

      .nav-scroller {
        position: relative;
        z-index: 2;
        height: 2.75rem;
        overflow-y: hidden;
      }

      .nav-scroller .nav {
        display: flex;
        flex-wrap: nowrap;
        padding-bottom: 1rem;
        margin-top: -1px;
        overflow-x: auto;
        text-align: center;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
      }
    </style>

    
    <!-- Custom styles for this template -->
    <link href="carousel.css" rel="stylesheet">
    <link href="heroes.css" rel="stylesheet">
  </head>
  <body>
    
<header>
  <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" >Eshara</a>
      
      
       
      </div>
    </div>
  </nav>
</header>
  
  <body>
    
<main>
  <h1 class="visually-hidden">Heroes examples</h1>

  <div class="px-4 py-5 my-5 text-center">
  <img class="d-block mx-auto mb-4" src="{{url_for('static', filename='la.png')}}" alt="" width="200" height="180">
    <h1 class="display-5 fw-bold">Fingerspelling with Eshara</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">We are always learning, and here at Eshara, we're committed to making that learning more accessible to everyone.It is an invaluable skill when communicating with deaf people in Kenya; so let's take some time to learn how to use it.Learn  finger spelling in Kenya Sign Language Today.</p>
      <p class="fw-bolder">SCROLL DOWN FOR SOME FUN!!</p>
      <p class="fw-semibold">Instructions</p>
      <p class="fst-italic">Match with the signs shown on the left</p>
      <p class="fst-italic">Sign anything you'd like!</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      </div>
    </div>
  </div>
  
  <table>
    <p class="fw-bolder">Kenyan Sign Language</p>
  <td><img src="{{url_for('static', filename='bitmap.png')}}" ></td>
  
   <td><p class="fw-bolder">Sign here!</p><img src="{{ url_for('video_feed') }}" id="video"></td>
    </table>
     
    </table> 
    <script>
      
      setInterval(updateFrame, 1000);
    </script>
  </body>
</html>
