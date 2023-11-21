from django.shortcuts import render
from django.http import HttpResponse

def screen(request):
    return HttpResponse("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Search</title>
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
    <style>
        body {
            font-family: 'Montserrat';
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        #brand-name {
            font-size: 50px;
            font-weight: bold;
            color: #4285f4; /* Google Blue */
            margin-bottom: 20px;
            user-select: none;
        }

        #search-container {
            text-align: center;
            background-color: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        #search-box-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #search-box {
            width: 600px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            margin-right: 8px;
            box-sizing: border-box;
            font-size: 15px;
            /*border-radius: 20px; /* Added border-radius for rounded corners */*/
        }

        #search-button {
            background-color: #4285f4; /* Google Blue */
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 15px;
        }

        #search-button:hover {
            background-color: #1a73e8; /* Google Dark Blue */
        }
    </style>
</head>
<body>

<div id="brand-name">ScrollGuard</div>

<div id="search-container">
    <div id="search-box-container">
        <input type="text" id="search-box" placeholder="Search...">
        <button id="search-button">Search</button>
    </div>
</div>

</body>
</html>


""")