from prettytable import PrettyTable
import model

# adding the rows with game info to the table
def adding_probability_data(table, date, standings, nba=True):
    
    # getting probabilites and converting them from numpy arrays to python lists
    probabilities, pred_games = model.get_probs(date, nba)
    probabilities = [list(prob) for prob in list(probabilities)]

    # iterates for however many games there are
    for i in range(len(probabilities)):

        # converting into percentages
        away_prob = probabilities[i][0] * 100
        home_prob = probabilities[i][1] * 100

        # whoever is >50% will obviously be the predicted winner
        if home_prob > 50:
            proj_winner = pred_games['Home'][i]
            proj_winner_percentage = home_prob
        else:
            proj_winner = pred_games['Away'][i]
            proj_winner_percentage = away_prob
        
        # team info for the left side of the table
        home_team_info = f"{pred_games['Home'][i]} ({standings[pred_games['Home'][i]]})"
        away_team_info = f"{pred_games['Away'][i]} ({standings[pred_games['Away'][i]]})"
        team_info = f"{home_team_info} vs {away_team_info}"

        # projected winner info for the right side of the table
        proj_winner_info = f"{proj_winner} ({proj_winner_percentage:.2f}%)"
        
        table.add_row([team_info, proj_winner_info])

    return table

def get_pretty_table(date, standings, nba=True):
    # data for PrettyTable
    table = PrettyTable()
    table.field_names = [f"NBA: {date}", "Projected Winners"] if nba else [f"WNBA: {date}", "Projected Winners"]
    table.align["Projected Winners"] = "c"
    table.horizontal_char = '-'

    table = adding_probability_data(table, date, standings, nba)
    return table
