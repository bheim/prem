from prem import Team
from league import League


teams_ratings = {"AFC Bournemouth": 74,
    "Arsenal": 81,
    "Aston Villa": 79,
    "Brentford": 75,
    "Brighton and Hove Albion": 77,
    "Chelsea": 83,
    "Crystal Palace": 76,
    "Everton": 77,
    "Fulham": 76,
    "Leeds United": 76,
    "Liverpool": 84,
    "Leicester City": 79,
    "Manchester City": 85,
    "Manchester United": 82,
    "Newcastle United": 79,
    "Nottingham Forest": 76,
    "Southampton": 75,
    "Tottenham Hotspur": 81,
    "West Ham United": 79,
    "Wolverhampton Wanderers": 78}
    
team_dict = {}

for name, rating in teams_ratings.items():
   team_dict[name] = Team(name, rating)


premier_league = League("Premier League", team_dict)
premier_league.create_table()

for c in range(2):
    for i, team_one in enumerate(premier_league.team_names):
        for team_two in premier_league.team_names[i + 1:]:
            print(premier_league.game_score(team_dict[team_one], team_dict[team_two]))

print(premier_league.create_table())
