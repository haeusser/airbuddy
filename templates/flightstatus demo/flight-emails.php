

<a href="flight-emails.php?send=invitation">Send E-Mail: Invitation</a>
<br>
<br>
<a href="flight-emails.php?send=delayed">Send E-Mail: Delayed</a>
<br>
<br>
<a href="flight-emails.php?send=soon">Send E-Mail: Soon</a>
<br>
<br>
<a href="flight-emails.php?send=arrival">Send E-Mail: Arrival</a>
<br>
<br>
<br>
<a href="flight-emails.php">Home</a>
<br>
<br>
<br>


<?php

/* --- Settings --- */
$send = $_GET['send'];
$from = "From: AirBuddy <updates@airbuddy.eu>\n";
$from .= "Content-Type: text/html\n";
$to = "co.thaiss@gmail.com";

/* --- E-Mail: Invitation --- */
if ($send == "invitation") {
    $message = '<!DOCTYPE html>
<html lang="de">
<head>
<link href=\'http://fonts.googleapis.com/css?family=Open+Sans:300,400,600\' rel=\'stylesheet\' type=\'text/css\'>
</head>
<body>
<h1 style="font-family: \'Myriad Pro Light\', \'Myriad Pro\', Calibri, Arial, sans-serif;"><span style="color:#040C39">Air</span><span style="color:#E6A901; font-weight:bold;">Buddy</span></h1>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Hello,</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">your friend invited you to pick him up, when he arrives at the airport.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Estimated arrival: 14th of November 2014, 4pm.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">There is nothing else to do. We will dynamically inform you about the flight status.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">If you don\'t want to get informed about your friend\'s flight, you can unsubscribe <a href="#">here</a>.</p> 
</body>
</html>';
    mail($to, "Your friend invited you to pick him up", $message, $from);
    echo "Die E-Mail 'Invitation' wurde erfolgreich verschickt!";
}

/* --- E-Mail: Delayed --- */
if ($send == "delayed") {
    $message = '<!DOCTYPE html>
<html lang="de">
<head>
<link href=\'http://fonts.googleapis.com/css?family=Open+Sans:300,400,600\' rel=\'stylesheet\' type=\'text/css\'>
</head>
<body>
<h1 style="font-family: \'Myriad Pro Light\', \'Myriad Pro\', Calibri, Arial, sans-serif;"><span style="color:#040C39">Air</span><span style="color:#E6A901; font-weight:bold;">Buddy</span></h1>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Hello,</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">your friend\'s flight is currently delayed by 30 minutes.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Thank you for picking him up!</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">If you don\'t want to get further updates on your friend\'s flight, you can unsubscribe <a href="#">here</a>.</p> 
</body>
</html>';
    mail($to, "Update on your friends flight: Delayed", $message, $from);
    echo "Die E-Mail 'Delayed' wurde erfolgreich verschickt!";
}

/* --- E-Mail: Soon --- */
if ($send == "soon") {
    $message = '<!DOCTYPE html>
<html lang="de">
<head>
<link href=\'http://fonts.googleapis.com/css?family=Open+Sans:300,400,600\' rel=\'stylesheet\' type=\'text/css\'>
</head>
<body>
<h1 style="font-family: \'Myriad Pro Light\', \'Myriad Pro\', Calibri, Arial, sans-serif;"><span style="color:#040C39">Air</span><span style="color:#E6A901; font-weight:bold;">Buddy</span></h1>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Hello,</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">your friend\'s flight is going to arrive in approximately 1hour.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Please make sure to be there on time. Thank you!</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">If you don\'t want to get further updates on your friend\'s flight, you can unsubscribe <a href="#">here</a>.</p> 
</body>
</html>';
    mail($to, "Update on your friends flight", $message, $from);
    echo "Die E-Mail 'Soon' wurde erfolgreich verschickt!";
}

/* --- E-Mail: Arrival --- */
if ($send == "arrival") {
    $message = '<!DOCTYPE html>
<html lang="de">
<head>
<link href=\'http://fonts.googleapis.com/css?family=Open+Sans:300,400,600\' rel=\'stylesheet\' type=\'text/css\'>
</head>
<body>
<h1 style="font-family: \'Myriad Pro Light\', \'Myriad Pro\', Calibri, Arial, sans-serif;"><span style="color:#040C39">Air</span><span style="color:#E6A901; font-weight:bold;">Buddy</span></h1>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Hello,</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">your friend\'s flight just arrived at the airport. He will arrive at gate no. 5.</p>
<p style="font-family: \'Open Sans\', Arial, sans-serfif; color:#333;">Thank you for your cooporation!</p>
</body>
</html>';
    mail($to, "Update on your friends flight: Arrival", $message, $from);
    echo "Die E-Mail 'Arrival' wurde erfolgreich verschickt!";
}


?>





