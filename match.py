from prem import Team
from league import League

premier_league = League()
premier_league.create_table()

for c in range(2):
    for i, team_one in enumerate(premier_league.team_names):
        for team_two in premier_league.team_names[i + 1:]:
            print(premier_league.game_score(premier_league.teams_ratings[team_one], premier_league.teams_ratings[team_two]))

print(premier_league.create_table())

premier_league.search_players() 
