from flask import Flask, render_template

from services.get_games import get_games

app = Flask(__name__)


@app.route('/')
def index():
    games_data = get_games()
    return render_template('index.html', data=games_data)



if __name__ == "__main__":
    app.run()
