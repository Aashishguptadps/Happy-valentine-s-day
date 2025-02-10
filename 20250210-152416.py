from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Valentine's Day Shiwani ❤️</title>
    <style>
        body {
            background-color: #ffebee;
            text-align: center;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .container {
            margin-top: 50px;
        }
        h1 {
            color: #d32f2f;
            font-size: 36px;
        }
        .heart {
            color: #e91e63;
            font-size: 100px;
            animation: heartbeat 1s infinite;
        }
        @keyframes heartbeat {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        p {
            font-size: 20px;
            color: #555;
        }
        .message {
            font-size: 22px;
            color: #d32f2f;
            font-weight: bold;
            margin-top: 20px;
        }
        .button {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 18px;
            color: white;
            background-color: #e91e63;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Happy Valentine's Day Shiwani! ❤️</h1>
        <div class="heart">💖</div>
        <p>Meri pyari Shiwani,</p>
        <p>Tum meri zindagi ka ek special hissa ho, <br> 
           Jo mujhe hamesha motivate karta hai, <br> 
           Tumhari muskurahat meri duniya roshan karti hai! 😊</p>
        
        <p class="message hidden">Aaj ke din bas yahi kehna hai...  
        <b>Main tumse dil se pyaar karta hoon! ❤️</b></p>

        <button class="button" onclick="showMessage()">Click to See My Love</button>
    </div>

    <script>
        function showMessage() {
            document.querySelector(".message").classList.remove("hidden");
        }
    </script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)