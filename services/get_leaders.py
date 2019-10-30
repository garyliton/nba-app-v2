from nba_api.stats.endpoints import leagueleaders


def get_leaders():
    leaders = leagueleaders.LeagueLeaders()
    leaders = leaders.data_sets[0]
    return leaders
