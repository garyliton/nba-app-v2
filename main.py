from flask import Flask, render_template, request
from services.get_games import get_games
from services.get_leaders import get_leaders
from services.get_updates import get_updates
from datetime import date

app = Flask(__name__)


@app.route('/')
def index():
    games_data = get_games()
    return render_template('index.html', data=games_data)


@app.route('/process_date_change', methods=['GET'])
def process_date_change():
    date_str = request.args['date']
    date_lst = date_str.split(" ")
    return {"games_data": get_games(date(int(date_lst[2]), int(date_lst[0]), int(date_lst[1])))}


@app.route('/league_leaders', methods=['GET'])
def league_leaders():
    leaders = get_leaders()
    leaders_data = []

    for player in leaders.data["data"]:
        player = player[1:4] + [player[8]] + [player[11]] + [player[14]] + player[17:22] + player[23:25]
        leaders_data.append(player)

    return render_template('league_leaders.html', data={"data": leaders_data, "headers": leaders.data["headers"]})


@app.route('/process_get_updates', methods=['GET'])
def process_get_updates():
    updates = get_updates()
    return {"updates": updates}


if __name__ == "__main__":
    app.run()
