def header():
    mobile = 'mobile'
    laptop = 'laptop'
    watch = 'watch'
    bags = 'bags'
    headphone = 'headphone'
    speakers = 'speakers'
    TShirts = 'T-Shirts'
    print(f"""

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="mainPage.py">SPOOL</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="mainPage.py">Home <span class="sr-only">(current)</span></a>
          </li>

          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Category
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" name='q' href="search.py?q={mobile}">Mobile</a>
              <a class="dropdown-item" name='q' href="search.py?q={watch}">Watches</a>
              <a class="dropdown-item" name='q' href="search.py?q={laptop}">Laptop</a>
              <a class="dropdown-item" name='q' href="search.py?q={bags}">Bags</a>
              <a class="dropdown-item" name='q' href="search.py?q={headphone}">Headphones</a>
              <a class="dropdown-item" name='q' href="search.py?q={speakers}">Speakers</a>
              <a class="dropdown-item" name='q' href="search.py?q={TShirts}">T-Shirts</a>
            </div>
          </li>
          <li class="nav-item">
            <a class="nav-link " href="cart.py" tabindex="-1" aria-disabled="true">MY CART</a>
          </li>
          <li class="nav-item">
            <a class="nav-link " href="loginPage.py" tabindex="-1" aria-disabled="true">login</a>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0" action='search.py'>
          <input class="form-control mr-sm-2" name="q" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>
    """)
def slide():
    print("""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    #mySidenav a {
      position: absolute;
      left: -100px;
      transition: 0.3s;
      padding: 15px;
      width: 130px;
      text-decoration: none;
      font-size: 20px;
      color: white;
      border-radius: 0 5px 5px 0;
    }

    #mySidenav a:hover {
      left: 0;
    }

    #about {
      top: 60px;
      background-color: #4CAF50;
    }

    #blog {
      top: 120px;
      background-color: #2196F3;
    }

    #projects {
      top: 180px;
      background-color: #f44336;
    }

    #contact {
      top: 240px;
      background-color: #555
    }
    
    #headphones {
      top: 300px;
      background-color: #2196F3
    }
    
    #speakers {
      top: 360px;
      background-color: #4CAF50
    }
    
    #tshirts {
      top: 420px;
      background-color: #f44336
    }
    </style>
    </head>
    <body>

    <div id="mySidenav" class="sidenav">
      <a name='q' href="search.py?q=mobile" id="about">MOBILES</a>
      <a name='q' href="search.py?q=watch" id="blog">WATCH</a>
      <a name='q' href="search.py?q=laptop" id="projects">LAPTOPS</a>
      <a name='q' href="search.py?q=bags" id="contact">BAGS</a>
      <a name='q' href="search.py?q=headphone" id="headphones">HEADPHONE</a>
      <a name='q' href="search.py?q=speakers" id="speakers">SPEAKERS</a>
      <a name='q' href="search.py?q=T-Shirts" id="tshirts">T-SHIRTS</a>
    </div>


    </body>
    </html> 

    """)


def footer():
    print("""
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    """)


