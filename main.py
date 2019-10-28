from flask import Flask, render_template

from services.get_games import get_games

app = Flask(__name__)


@app.route('/')
def index():
    x = get_games()
    return render_template('index.html')



if __name__ == "__main__":
    app.run()
