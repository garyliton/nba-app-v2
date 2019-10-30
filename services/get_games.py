from nba_api.stats.endpoints import ScoreboardV2
from datetime import date
from services.team_img import constants

def get_games():
    scoreboard = ScoreboardV2(game_date=date.today())
    linescores = scoreboard.line_score
    gameday_data = []
    current_game = {}
    count = 0
    for linescore in linescores.data['data']:
        if (count % 2) == 0:
            current_game['away'] = {
                'GAME_ID': linescore[2],
                'TEAM_ID': linescore[3],
                'TEAM_ABBREVIATION': linescore[4],
                'TEAM_CITY_NAME': linescore[5],
                'TEAM_NAME': linescore[6],
                'TEAM_WINS_LOSSES': linescore[7],
                'PTS': linescore[22],
                'IMG': constants[linescore[4]]['img']
            }

        else:
            current_game['home'] = {
                'GAME_ID': linescore[2],
                'TEAM_ID': linescore[3],
                'TEAM_ABBREVIATION': linescore[4],
                'TEAM_CITY_NAME': linescore[5],
                'TEAM_NAME': linescore[6],
                'TEAM_WINS_LOSSES': linescore[7],
                'PTS': linescore[22],
                'IMG': constants[linescore[4]]['img']
            }
            gameday_data.append(current_game)
            current_game = {}
        count += 1

    return gameday_data