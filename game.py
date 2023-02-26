"""Contains Game class."""


class Game:
    """
    Game class.

    Contains variables and methods related to the game itself.
    """

    # Might need to add more variables here later.
    # Should the dice/player/intelligence- objects be passed
    # as arguments here or somewhere else?
    # Easier to decide when the shell is in place.
    def __init__(self, number_of_players: int):
        """
        Initiate a game with default settings.

        Initiates a game with either one player against the
        computer or two players against eachother.
        Settings can be changed after the game is initialized.
        """
        if (number_of_players > 0 and number_of_players < 3):
            self._number_of_players = number_of_players
        else:
            raise ValueError("Invalid input. There can only be 1-2 players.")

        self._score_to_win = 100
        self._number_of_die = 1
        # Not sure how to implement a change in backroundcolor
        # but it might not be that difficult.
        self._backround_color = "Default"

    def set_number_of_players(self, number_of_players: int):
        """Change the number of players in the game."""
        if (number_of_players > 0 and number_of_players < 3):
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
