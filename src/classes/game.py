#Class Game

class Game():
    def __init__(self):
        self.n = 0
    
    def update(self):
        self.n += 1
    
    def print_game(self, scoreboard):
        print("GAME OVER") 
        print("SCORE GAME ", self.n, ": ", scoreboard.score, "\n")

    def print_games(self):
        print("TOTAL GAMES: ", self.n, "\n")
        