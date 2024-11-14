#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

print "Content-type: text/html\n\n";

# Access form elements
# ------ NAME ----------------------
my $fname = param('fname');
my $lname = param('lname');

# ------ ADDRESS -------------------
my $street = param('street');
my $city = param('city');
my $pc = param('postalcode');
my $province = param('province');

# ------ CONTACT INFO --------------
my $phone = param('phone');
my $email = param('email');

# ------ ROOM SELECTION --------------
my $room = param('room');

# ------ PICTURE UPLOAD --------------
my $picture = param('picture');
# Save the uploaded image file
my $upload_dir = "../Lab07"; # Change this to your desired directory
my $upload_file = "$upload_dir/$picture";
if ($picture) {
    my $upload_fh = upload('picture');
    open my $out_fh, '>', $upload_file or die "Cannot open $upload_file: $!";
    binmode $out_fh;
    while (<$upload_fh>) {
        print $out_fh $_;
    }
    close $out_fh;
}

print <<HTML;
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escape Room Registration Form Complete</title>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Allerta+Stencil&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Cedarville+Cursive&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Quicksand:wght@300..700&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <style>
        *{
            font-family: "Open Sans", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            font-variation-settings: "wdth" 100;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        .profile-pic {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            display: block;
            margin: 0 auto 20px;
        }

        .success{
            padding-top:1%; 
            padding-bottom: 0;
            font-weight: 500; 
            font-weight: bold;
            color: #bfd200; 
            font-family: Allerta Stencil, sans-serif; 
            font-style: normal;
            font-size: 3rem;
            margin-bottom: 0;
            text-align: center;
        }

        .container{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .postcard{
            background-color: white;
            padding: 3rem;
            width: 70%;
            text-align: center;
            border-width: 1.5rem;
            border-color: #042d3a;
            border-style: solid;
        }

        #name{
            font-size: 2rem;
            padding: 2%;
        }

        #name > #r{
            color: #042d3a;
            font-weight: bold;
        }

        #name > #n{
            color: #bfd200;
            font-weight: bold;
        }

        #name > p{
            font-size: 2rem;
            padding: 2%;
            color: white;
        }

        .err{
            color: magenta;
        }

        a{
            color:magenta;
        }

        h3{
            color: #042d3a;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="postcard">

HTML

    # Display uploaded image if available
    if ($picture) {
        print "<img src='../Lab07/$picture' class='profile-pic' alt='Uploaded Picture'>";
    }
    # ------------- PROCESSING NAME ELEMENTS ---------------------------------------------------
    
    print "<h1 class='success'>SUCCESS</h1>";
    print "<h1 id='name'>Thanks for registering for <span id='r'>$room</span>, <span id='n'><br>$fname $lname</span></h1>";
    print "<p>Confirm your details below. If there are any issues or concerns, please return to the registration form <a href='../Lab07/lab07b.html'>here</a>.</p>";

    # ------------ PROCESSING ADDRESS ELEMENTS ------------------------------------------------
    # Street Name
    if ($street =~ /^[A-Za-z0-9\s]+$/ && $city =~ /^[A-Za-z0-9\s]+$/ && $province =~ /^[A-Za-z0-9\s]+$/){
        print "<h3><br>$street</h3>";
        print "<h3>$city, $province</h3>";
    } else{
        print "<h3 class='err'><br>Error! Street field cannot be blank.</h3>";
    }

    # Postal Code: X#X #X#
    if ($pc =~ /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/){
        print "<h3>$pc</h3>";
    } else{
        print "<h3 class='err'><br>Error! Incorrect postal code format. Must be in the form L0L 0L0.</h3>";
    }

    # ------------- PROCESSING CONTACT INFORMATION -------------------------------------------
    # Phone Number
    if ($phone =~ /^\d{10}$/){
        print "<h3><br>$phone</h3>";
    } else{
        print "<h3 class='err'><br>Error! Incorrect phone number format.</h3>";
    }
    
    # Email Address
    if ($email =~ /^.+@.+\./){
        print "<h3><br>$email</h3>";
    } else{
        print "<h3 class='err'><br>Error! Incorrect email address format.</h3>";
    }
    print <<HTML;
    </div>
</div>
</body>
</html>
HTML