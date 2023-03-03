from random import randint
from prem import Team, Player
import pandas as pd
#This initializes the whole league with teams
class League:

    def __init__(self):
        self.name = "Premier League"
        self.table = {}
        self.team_names = []

        self.teams_ratings = {"AFC Bournemouth": 74,
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
        

        for name, rating in self.teams_ratings.items():
            self.teams_ratings[name] = Team(name, rating)
        
        #getting players in teams
        players = pd.read_csv("players_update.csv")
        for _, row in players.iterrows():
            self.teams_ratings[row['Club']].players[row['Name']] = Player(row['Name'], int(row['Ratings']), row['Position'])

        for team in self.teams_ratings.keys():
            self.team_names.append(team)

        for name in self.teams_ratings.keys():
            self.table[name] = 0
    
    #algo for determing difference
    def diff_factor(team_one, team_two):
        random_change = randint(-2, 2)
        return round((team_one.rating - team_two.rating + random_change)/4)

    #game function with no score, random score will be generated using rating systems
    #what if rating changed depending on score? Like we have a predicted score, and if it differs, rating is altered?
    def game_score(self, team_one, team_two):

        diff = League.diff_factor(team_one, team_two)

        score = [randint(0, 3 + diff), randint(0, 3 - diff)]
        first, second = score

        if first > second:
            team_one.win(first, second)
            team_two.loss(second, first)
            return(f"{team_one.get_name()} beat {team_two.get_name()} {score[0]} to {score[1]}!")
        elif first < second:
            team_one.loss(first, second)
            team_two.win(second, first)
            return(f"{team_one.get_name()} lost to {team_two.get_name()} {score[0]} to {score[1]}!")
        else:
            team_one.draw()
            team_two.draw()
            return(f"{team_one.get_name()} drew with {team_two.get_name()} {score[0]} to {score[1]}!")

    #need to implement goal-differential
    def create_table(self):
        #Creates list of tuples, then sorts
        team_lst = []

        for team in self.table.keys():
            self.table[team] = self.teams_ratings[team].get_points()
   
        for k, v in self.table.items():
            team_lst.append((k, v))

        for i in range(len(team_lst)):
            for j in range(len(team_lst) - 1):
                if team_lst[j][1] < team_lst[j + 1][1]:
                    team_lst[j], team_lst[j + 1] = team_lst[j + 1], team_lst[j]

        return team_lst

    def search_players(self):
        for team in self.team_names:
            for player in self.teams_ratings[team].players.values():
                print(f"{player.name} plays for {team} and is rated {player.rating} "
                      f"and their worth is {player.worth:,}")
