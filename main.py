from standings import get_standings
import pretty_table

def main(date = None, nba=True):
    standings = get_standings(nba)

    try:
        # getting the probabilities in the prettyTable format
        table_data = pretty_table.get_pretty_table(date, standings, nba)
        print(table_data)
    except KeyError:
        # if date has no (w)nba games
        print(f"{date} has no {"nba" if nba else "wnba"} games")
    except Exception as e:
        # if some other error has occurred
        print(f"an error has occurred: {e}")
    return

if __name__ == "__main__":
    main(date="06/17/2024", nba=True)