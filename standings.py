from nba_api.stats.endpoints import leaguestandingsv3
import numpy as np

def get_standings(nba=True):
    id = "00" if nba else "10"
    season = "2023-24" if nba else "2024"

    data = leaguestandingsv3.LeagueStandingsV3(league_id=id, season=season).get_data_frames()[0]

    categories = ["TeamCity", "TeamName", "WINS", "LOSSES"]
    data = data[categories]

    data = [list(np.array(team)) for team in list(np.array(data))]

    standings = {}
    for team in data:
        name = f"{team[0]} {team[1]}"
        record = f"{team[2]}-{team[3]}"

        standings[name] = record
    
    return standings
