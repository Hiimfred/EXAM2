"""Contains Game class."""
from player import Player
from intelligence import Intelligence


class Game:
    """
    Game class.

    Contains variables and methods related to the game itself.
    """

    def __init__(self):
        """
        Initiate a game with default settings.

        Initiates a game with either one player against the
        computer or two players against eachother.
        Settings can be changed after the game is initialized.
        """
        self._number_of_players = 1
        self._score_to_win = 100
        self._number_of_die = 1
        # magenta as default for text?
        self._text_color = "magenta"

    def player_vs_player(player1: Player, player2: Player):
        ...

    def solo_play(player1: Player, NPC: Intelligence):
        ...

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