from prem import Team
from league import League

premier_league = League()
premier_league.create_table()
for gamedays in range(38):
    for n in range(len(premier_league.team_names)//2):
        team_one = premier_league.team_names[n]
        team_two = premier_league.team_names[len(premier_league.team_names) - 1 - n]
        print(premier_league.game_score(premier_league.teams_dic[team_one], premier_league.teams_dic[team_two]))
    premier_league.team_names.insert(0, premier_league.team_names.pop())


team = input("Please choose a time to manage. You must type the name exactly!")
while True:
    try:
        premier_league.teams_dic[team].user = True
        print("Wonderful choice! You're the manager of {team}")
        break
    except KeyError: 
        print("That's not a real team. Try again!")

for n in range(365):
    #we are simulating a year!
    #We probably want to report the current day. We can start on the first day of the league
    print(f"It's day {n} of the league. This is week {n // 7 + 1} of the league.")
    if n //7 <= 37:
        print("It's game day!")
    #The way this works: they choose their lineup, see who they're player,
    #play and get a result. 

    #needs to be a command that leads to continue like next

