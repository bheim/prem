from random import randint

class League:

    def __init__(self, name, teams):
        self.name = name
        assert type(teams) is dict
        self.teams = teams
        self.table = {}
        self.team_names = []

        for team in teams.keys():
            self.team_names.append(team)

        #important to note that the only way to access the team objects is through the teams dictionary!
        for name in self.teams.keys():
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
            self.table[team] = self.teams[team][0].get_points()
   
        for k, v in self.table.items():
            team_lst.append((k, v))

        for i in range(len(team_lst)):
            for j in range(len(team_lst) - 1):
                if team_lst[j][1] < team_lst[j + 1][1]:
                    team_lst[j], team_lst[j + 1] = team_lst[j + 1], team_lst[j]

        return team_lst

       
    



        
