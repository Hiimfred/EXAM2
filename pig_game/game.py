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
    _current_player = "Not Set"
    _pending_player = "Not set"
    _bot = Intelligence()
    _game_started = False
    _prior_game = False
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

    def get_score_left(self, score: int):
        return self._score_to_win - score

    def start_solo_game(self, name):
        self._game_started = True
        self._current_player = Player(name, "blue")
        self._bot = Intelligence()
        self.set_number_of_players(1)
        return

    def start_multiplayer_game(self, name1, name2):
        self._game_started = True
        self.set_number_of_players(2)
        self._current_player = Player(name1, "blue")
        self._pending_player = Player(name2, "red")
        return

    def roll(self):
        outcome = 0
        outcome = self._current_player.roll(self._die)
        msg = f"\t{self._current_player.get_name()} rolled a {outcome}..\n"
        return msg, outcome

    def begin_bot_turn(self):
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
        self._current_player.hold()
        new_total = self._current_player.get_total_score()
        msg_p1 = "\tYou choose to hold!"
        msg_p2 = f" Your new total is {new_total}.\n"

        return msg_p1 + msg_p2

    def pass_turn(self):
        temp = self._current_player
        self._current_player = self._pending_player
        self._pending_player = temp

        return f"\n\tIt is your turn to roll{self._current_player.get_name()}!"

    def is_winner(self):
        _is_winner = False
        max_score = self.get_score_to_win()

        if (self._current_player.get_total_score() >= max_score):
            _is_winner = True
            self._winner = self._current_player
            self._current_player.add_win()
        elif (self._bot.get_total_score() >= max_score):
            _is_winner = True
            self._winner = self._bot

        return _is_winner

    def get_winner(self):
        return self._winner

    def get_current_player_name(self):
        return self._current_player.get_name()

    def game_is_running(self):
        return self._game_started

    def end_game(self):
        self._game_started = False
        self._prior_game = True

    def is_prior_game(self):
        return self._prior_game

    def reset_game(self):
        self._current_player.set_total_score(0)

        if (self.get_number_of_players() == 1):
            self._bot.set_total_score(0)
        else:
            self._pending_player.set_total_score(0)

        self._game_started = True

    def save_highscore(self):
        ...

    def load_highscore(self):
        ...
