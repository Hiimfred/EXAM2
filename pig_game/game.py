"""Contains Game class."""
from .player import Player
from .intelligence import Intelligence
from .dice import Dice
from .highscore import Highscore
from .difficulty import Difficulty


class Game:
    """
    Game class.

    Contains variables and methods related to the game itself.
    """

    _highscore = Highscore()
    _current_player = "Not Set"
    _pending_player = "Not set"
    _bot = Intelligence()
    _game_started = False
    _prior_game = False
    _winner = "Not set"

    def __init__(self):
        """Initiate a game with default settings."""
        self._number_of_players = "Not set"
        self._score_to_win = 100
        self._text_color = "magenta"
        self._die = Dice()

    def set_number_of_players(self, number_of_players: int):
        """Change the number of players in the game."""
        if (number_of_players == 1 or number_of_players == 2):
            self._number_of_players = number_of_players
        else:
            raise ValueError("Invalid input. There can only be 1-2 players.")

    def get_number_of_players(self):
        """Return the number of players in the game."""
        return self._number_of_players

    def set_score_to_win(self, score_to_win: int):
        """Change the score needed to win the game."""
        self._score_to_win = score_to_win

    def get_score_to_win(self):
        """Return the score needed to win the game."""
        return self._score_to_win

    def start_solo_game(self, name):
        """Initiate a game with one player."""
        self._game_started = True
        self._current_player = Player(name, "blue")
        self.set_number_of_players(1)
        return

    def start_multiplayer_game(self, name1, name2):
        """Initiate a game with two players."""
        self._game_started = True
        self._current_player = Player(name1, "blue")
        self._pending_player = Player(name2, "red")
        self.set_number_of_players(2)
        return

    def roll(self):
        """Roll the current players dice, return message and outcome."""
        outcome = 0
        outcome = self._current_player.roll(self._die)
        msg = f"\t{self._current_player.get_name()} rolled a {outcome}..\n"
        return msg, outcome

    def begin_bot_turn(self):
        """Initiate bots turn and return message containing the result."""
        outcome = 0
        msg = ""

        outcomes = self._bot.make_play(self._current_player)
        if (1 in outcomes):
            msg = "\n\tThe bot rolled a 1"
        else:
            msg = "\n\tThe bot rolled"
            for outcome in outcomes:
                msg += f", {outcome}"

        return msg + f". His score is now {self._bot.get_total_score()}!\n"

    def hold(self):
        """Hold current players score and return the new total."""
        self._current_player.hold()
        new_total = self._current_player.get_total_score()
        msg_p1 = "\tYou choose to hold!"
        msg_p2 = f" Your new total is {new_total}.\n"

        return msg_p1 + msg_p2

    def pass_turn(self):
        """Change the current player and return a message."""
        temp = self._current_player
        self._current_player = self._pending_player
        self._pending_player = temp

        return f"\tYour turn to roll {self._current_player.get_name()}!\n"

    def is_winner(self):
        """Check if someone has reached the score limit and return result."""
        _is_winner = False
        max_score = self.get_score_to_win()
        player_score = self._current_player.get_total_score()
        player_score += self._current_player.get_score()

        if (player_score >= max_score):
            _is_winner = True
            self._winner = self._current_player
            self._current_player.add_win()
            self._highscore.add_entry(self._current_player)
        elif (self._bot.get_total_score() >= max_score):
            _is_winner = True
            self._winner = self._bot

        return _is_winner

    def get_winner(self):
        """Return the Player/Intelligence object that is the winner."""
        return self._winner

    def get_current_player_name(self):
        """Return the current players name."""
        return self._current_player.get_name()

    def game_is_running(self):
        """Return whether or not the game is running."""
        return self._game_started

    def end_game(self):
        """End the game and set variable to show that there is a prior game."""
        self._game_started = False
        self._prior_game = True

    def is_prior_game(self):
        """Return whether or not there is a prior game."""
        return self._prior_game

    def reset_game(self):
        """Reset the scores and start the game."""
        self._current_player.set_total_score(0)

        if (self.get_number_of_players() == 1):
            self._bot.set_total_score(0)
        else:
            self._pending_player.set_total_score(0)

        self._game_started = True

    def display_highscore(self):
        """If there is a highscore then return it."""
        msg = "\tThere are no highscores.\n"

        if (self._highscore.not_empty()):
            return self._highscore.get_highscore()
        else:
            return msg

    def call_save_highscore(self):
        """Save the highscore."""
        self._highscore.save_highscore()

    def new_difficulty(self):
        """Change the difficulty of the bot to either EASY or HARD."""
        msg = ""

        if (self._bot.get_difficulty() is Difficulty.EASY):
            self._bot.set_difficulty(Difficulty.HARD)
            msg = "\tBot difficulty set to HARD.\n"
        else:
            self._bot.set_difficulty(Difficulty.EASY)
            msg = "\tBot difficulty set to EASY.\n"

        return msg
