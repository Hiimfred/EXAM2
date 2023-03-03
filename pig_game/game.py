"""Contains Game class."""
from player import Player
from intelligence import Intelligence
from dice import Dice


class Game:
    """
    Game class.

    Contains variables and methods related to the game itself.
    """
    # Probably need to initiate player/npc objects in do_solo/multiplayer.
    _current_player = Player("Not set", "blue")
    _pending_player = Player("Not set", "red")
    _bot = Intelligence()
    _game_started = False
    _winner = "Not set"

    def __init__(self):
        """
        Initiate a game with default settings.

        Initiates a game with either one player against the
        computer or two players against eachother.
        Settings can be changed after the game is initialized.
        """
        self._number_of_players = 1
        self._score_to_win = 100
        self._text_color = "magenta"
        self.die = Dice()

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

    def get_score_left(self, score: int):
        return self._score_to_win - score

    def start_solo_game(self, name):
        self.game_started = True
        self._current_player.set_name(name)
        self.set_number_of_players(1)
        return

    def start_multiplayer_game(self, name1, name2):
        self.game_started = True
        self.set_number_of_players(2)
        self._current_player.set_name(name1)
        self._pending_player.set_name(name2)
        return

    def roll(self):
        outcome = self._current_player.roll()
        msg = f"{self._current_player.get_name()} rolled a {outcome}.."
        return msg

    def begin_bot_turn(self):
        msg = ""

        outcomes = self._bot.make_play()
        if (1 in outcomes):
            msg = "The bot rolled a 1!"
        else:
            msg = "The bot rolled "
            for outcome in outcomes:
                msg += f"{outcome}, "
            msg += ".\n"

        return msg + f"His score is now {self._bot.get_total_score()}!"

    def hold(self):
        new_total = self._current_player.hold()
        msg_p1 = "You choose to hold!"
        msg_p2 = f" Your new total is {new_total}."

        return msg_p1 + msg_p2

    def pass_turn(self):
        temp = self._current_player
        self._current_player = self._pending_player
        self._pending_player = temp

        return f"Now it is {self._current_player}s turn to roll!"

    def check_for_winner(self):
        _is_winner = False
        max_score = self.get_score_to_win()

        if (self._current_player.get_total_score() >= max_score):
            _is_winner = True
            self._winner = self._pending_player
        elif (self._bot.get_total_score() >= max_score):
            _is_winner = True
            self._winner = self._bot

        return _is_winner

    def get_winner(self):
        return self._winner
