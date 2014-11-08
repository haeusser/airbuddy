

<!DOCTYPE html>
<!--[if IE 7]><html class="ie7"><![endif]-->
<!--[if IE 8]><html class="ie8"><![endif]-->
<html lang="de">
    
    <head>

        <meta charset="utf-8" />
        <title>AirBuddy - there is no better way to travel to your friends</title>

        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <meta name="author" content="Coinlex Webdesign" />
        <meta name="robots" content="index, follow" />

        <meta name="audience" content="all"/>
        <meta name="language" content="de" />
        <meta name="author" content="Coinlex Webdesign" />
        <meta name="copyright" content="All Rights reserved! Copyright by Coinlex Webdesign!" />

        <link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,600' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Ubuntu' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" media="screen" href="../static/css/style.css" />
        <link rel="stylesheet" type="text/css" media="print" href="../static/css/print.css" />
        <link rel="shortcut icon" href="../static/images/favicon.ico" />

    </head>

    <body>
        
        <div id="page-content-subpage">
            
            <img id="img-logo-simple" src="../static/images/airbuddy-logo-simple.png" alt="">
            <br>
            <br>
            <p>
                <span class="current-location">Geschwister-Scholl-Platz 1, München</span><br>
                <span class="nearest-airport">Munich Airport</span>
            </p>
            <br>
            <br>
            <table>
                <tr>
                    <td><h5>London</h5></td>
                    <td class="price">99$</td>
                    <td><a class="btn-getticket" href="#">Get ticket!</a></td>
                </tr>
                <tr>
                    <td><img src="../static/images/facebook/fb-1.png"><br>Katja Huber</td>
                    <td><img src="../static/images/facebook/fb-2.png"><br>Steve Johnson</td>
                    <td><img src="../static/images/facebook/fb-3.png"><br>Maik Abs</td>
                </tr>
            </table>
            <br>
            <br>
            <table>
                <tr>
                    <td><h5>New York</h5></td>
                    <td class="price">699$</td>
                    <td><a class="btn-getticket" href="#">Get ticket!</a></td>
                </tr>
                <tr>
                    <td><img src="../static/images/facebook/fb-4.png"><br>Linda Jason</td>
                    <td><img src="../static/images/facebook/fb-5.png"><br>Niclas White</td>
                    <td><img src="../static/images/facebook/fb-6.png"><br>Yun Han</td>
                </tr>
                <tr>
                    <td><img src="../static/images/facebook/fb-7.png"><br>Lea Bauer</td>
                    <td><img src="../static/images/facebook/fb-8.png"><br>Peter Jobs</td>
                    <td></td>
                </tr>
            </table>
            
        </div>
        

        <table>
            {% for airport in prices %}
            <tr>
                <td><h5>{% block loop_item scoped %}{{ airport }}</h5></td>
                <td>{{ prices[airport] }}</td>
                <td><a class="btn-getticket" href="#">Get ticket!</a></td>
            </tr>
            <tr>
                {% for friend in airports[airport] %}
                {% block loop_item2 scoped %}
                <td>{{ friend['id'] }}<br>{{ friend['name'] }}<br>{{ friend['location']['name'] }}</td>
                {% endblock %}{% endfor %}
            </tr>
            {% endblock %}
            {% endfor %}
        </table>
        <script type="text/javascript" src="../static/js/retina/retina.js"></script>
    
    </body>

</html>