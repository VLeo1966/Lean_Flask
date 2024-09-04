from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <head>
        <title>Текущее время</title>
        <meta http-equiv="refresh" content="1">
    </head>
    <body>
        <h1>Текущая дата и время: {current_time}</h1>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)

