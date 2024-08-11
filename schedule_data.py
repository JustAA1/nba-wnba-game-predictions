import requests
import pandas as pd

def get_data(date_for_predictions, nba=True):
    nba_link = "https://cdn.nba.com/static/json/staticData/scheduleLeagueV2_1.json"
    wnba_link = "https://cdn.wnba.com/static/json/staticData/scheduleLeagueV2_1.json"
    
    link_to_use = nba_link if nba else wnba_link
    preseason_date = "10/24/2023" if nba else "05/14/2024"

    json_data = requests.get(url=link_to_use).json()

    date_and_data = {}

    game_date_data = json_data['leagueSchedule']['gameDates']
    for data in game_date_data:
        data_to_add = []

        date = data['gameDate'].split(" ")[0]

        games_on_date = data['games']
        for game in games_on_date:

            game_date_tine = game['gameDateTimeEst']
            game_date, game_time_est = tuple(game_date_tine.split("T"))
            game_date = game_date.replace("-", "/")
            temp = game_date[:4]
            game_date = f"{game_date[5:]}/{temp}"
            game_time_est = game_time_est[:-1]

            arena_name = game['arenaName']

            home_team_data = game['homeTeam']
            away_team_data = game['awayTeam']

            home_team_id = home_team_data['teamId']
            away_team_id = away_team_data['teamId']

            home_team_name = f'{home_team_data['teamCity']} {home_team_data['teamName']}'
            away_team_name = f'{away_team_data['teamCity']} {away_team_data['teamName']}'

            home_score = home_team_data['score']
            away_score = away_team_data['score']

            home_win = None
            if home_score > away_score:
                home_win = True
            elif away_score > home_score:
                home_win = False

            info_to_add = {"Away": away_team_name, "AwayTeamID": away_team_id, 
                            "Home": home_team_name, "HomeTeamID": home_team_id, 
                            "Arena": arena_name, "HomeWin": home_win, "Start (ET)": game_time_est}
            
            data_to_add.append(info_to_add)
        
        date_and_data[date] = data_to_add

    date_and_data_keys = list(date_and_data.keys())
    for key in date_and_data_keys:
        if key == preseason_date:
            break
        del date_and_data[key]
    
    data_for_df = []
    date_and_data_keys = list(date_and_data.keys())

    bool_to_break = False
    for key in date_and_data_keys:
        games = date_and_data[key]
        for game in games:
            if game['HomeWin'] is None:
                bool_to_break = True
                break
        if bool_to_break:
            break
        data_for_df += games

    df_total_data = pd.DataFrame(data_for_df)
    df_prediction_data = pd.DataFrame(date_and_data[date_for_predictions])
    return df_prediction_data, df_total_data
