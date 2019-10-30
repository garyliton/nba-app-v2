from nba_api.stats.endpoints import ScoreboardV2

game_ids = []


def get_updates():
    scoreboard = ScoreboardV2()
    linescores = scoreboard.line_score
    result = []
    count = 0
    game_id = ''
    away_abv = ''
    away_pts = 0
    away_4pts = 0
    home_abv = ''
    home_pts = 0
    home_4pts = 0
    for linescore in linescores.data['data']:
        if (count % 2) == 0:
            game_id = linescore[2]
            away_abv = linescore[4]
            if linescore[22] == None:
                away_pts = 0
            else:
                away_pts = linescore[22]
            if away_4pts == None:
                away_4pts = 0
            else:
                away_4pts = linescore[11]
        else:
            home_abv = linescore[4]
            if linescore[22] == None:
                home_pts = 0
            else:
                home_pts = linescore[22]
            if away_4pts == None:
                home_4pts = 0
            else:
                home_4pts = linescore[11]

        if (count % 2) != 0:
            if (away_4pts != 0 and home_4pts != 0) and (abs(away_pts - home_pts) < 30):
                if game_id not in game_ids:
                    game_ids.append(game_id)
                    result.append("hey watch this game: " + str(away_abv) + " " + str(away_pts) +
                                  " VS " + str(home_abv) + " " + str(home_pts))
        count += 1

    if result:
        return result
    return None


