import pandas as pd


def csv_to_parquet(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_parquet(csv_file_path.replace('.csv', '.parquet'), engine='pyarrow')


csv_to_parquet('data/8478402.csv')



'''
Train the model on the following data:
- 5 years of data 2020-2025
- Team Game Data (Oilers Only, every game from 2020-2025) EDM.csv
    - opposingTeam
    - xGoalsPercentage 5 on 5
    - xGoalsFor 5 on 5
    - xGoalsAgainst 5 on 5
    - xGoalsPercentage PP
    - xGoalsFor PP
    - xGoalsAgainst PP
    - xGoalsPercentage SH
    - xGoalsFor SH
    - xGoalsAgainst SH
    - Goalie
    - Home/Away
    - Date
- Team data (NOT game specific, just overall team data for each season 2020-2025) teams.csv
    - 5 on 5 xGoalsFor
    - 5 on 5 xGoalsAgainst
    - PP xGoalsFor
    - PP xGoalsAgainst
    - SH xGoalsFor
    - SH xGoalsAgainst
    - Season
- Mcdavid Player Data (every game from 2020-2025) 8478402.csv
    - Date
    - Opposing Team
    - Home/Away
    - Shift Count
    - TOI
    - Goals
    - Assists
    - Points
    - xGoals
    - xAssists
    - xPoints
    - Shots
    - Shot Attempts
    - Fenwick For
    - Fenwick Against
    - Corsi For
    - Corsi Against
    - High Danger Chances For
    - High Danger Chances Against
    - Giveaways
    - Takeaways
    - Hits For
    - Hits Against    

INPUT to model:
- game details ie Oilers vs Canucks
- I want expected points for McDavid in that game
OUTPUT from model:
- expected points for McDavid in that game
- compare to bet365 over under line for points in that game

model : transformer based model
'''