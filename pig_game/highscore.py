class Highscore:
    ''''Construktor for keeping the score '''
    def __init__(self, player_name):
        self.player_name = player_name
        self.bot_name = "Bot"
        self.player_score = 0
        self.bot_score = 0
    ''''getters and setters for the player and the bot'''
    def setPlayer_score(self, score):
        self.player_score += score

    def setBot_score(self, score):
        self.bot_score += score

    def getplayer_score(self):
        return self.player_score

    def getbot_score(self):
        return self.bot_score

    def print_scoreboard(self):
        print(f"Scoreboard for {self.player_name}")
        print(f"{self.player_name}: {self.getplayer_score()}")
        print(f"{self.bot_name}: {self.getbot_score()}")