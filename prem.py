class Team:

    #add goal-differential!
    def __init__(self, name):
        self.name = name
        self.goal_differential = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.rating = 0
        self.players = {}
        user = False


    def add_player(self, person):
        assert isinstance(person, Player)
        self.players[person.name] = person
    
    def show_players(self):
        for player, info in self.players.items():
            print(f"{player} is rated {info.high_rating}")

    def get_rating(self):
        ratings = []
        total = 0
        for player in self.players.values():
            ratings.append(player.high_rating)
        ratings.sort(reverse=True)
        for n in range(15):
            total += ratings[n]
        self.rating = total // 15
        
    
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
    
class Player:

    def __init__(self, name, rating, position):
        self.name = name
        self.positions = []
        self.high_rating = rating
        self.worth = round((1.1)**(rating - 40)*1000000, 0)

        #rating calculations
        if "att" in position:
            self.positions.append("att")
            self.att_rating = rating
            self.gk_rating = 0
        if "mid" in position:
            self.positions.append("mid")
            self.mid_rating = rating
            self.gk_rating = 0
        if "def" in position:
            self.positions.append("def")
            self.def_rating = rating
            self.gk_rating = 0
        if "gk" in position:
            self.positions.append("gk")
            self.att_rating = 0
            self.mid_rating = 0
            self.def_rating = 0
            self.gk_rating = rating
        
        if "mid" in self.positions:
            if "att" not in self.positions:
                self.att_rating = rating * .75
            if "def" not in self.positions:
                self.def_rating = rating * .75
        
        if "att" in self.positions:
            if "mid" not in self.positions:
                self.mid_rating = rating * .75
            if "def" not in self.positions:
                self.def_rating = rating * .5
        
        if "def" in self.positions:
            if "mid" not in self.positions:
                self.mid_rating = rating * .75
            if "att" not in self.positions:
                self.att_rating = rating * .5
    
