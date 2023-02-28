class Team:

    #add goal-differential!
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.goal_differential = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    
    def get_points(self):
        return self.wins * 3 + self.draws * 1
    
    def win(self, my_score, their_score):
        self.goal_differential += my_score - their_score
        self.wins += 1

    def loss(self, my_score, their_score):
        self.goal_differential += my_score - their_score
        self.losses += 1
    
    def draw(self):
        self.draws += 1

    def get_name(self):
        return self.name

    def get_games_played(self):
        return self.wins + self.draws + self.losses
    


    
