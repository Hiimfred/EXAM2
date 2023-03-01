"""Contains a player class."""
from dice import Dice


class Player():
    """
    PLAYER CLASS.

    CONTAINS GETTERS AND SETTERS FOR NAME, SCORE AND COLOR
    AND A CLASS MAKE_PLAY FOR THE PLAYER TO MAKE A MOVE IN THE GAME.
    """

    color_list = ["red", "blue", "green", "magenta", "yellow", "cyan"]

    def __init__(self, name: str, color: str):
        """DEFAULT PLAYER BLUEPRINT."""

        self._total_score = 0
        self._current_score = 0
        self._name = name
        self._color = color

    def get_name(self):
        """GET THE PLAYER NAME."""
        return self._name

    def set_name(self, new_name: str):
        """SET THE PLAYER NAME WHEN ENTERED."""
        self._name = new_name

    def get_score(self):
        """GET THE PLAYER CURRENT SCORE."""
        return self._current_score

    def set_score(self, score):
        """SET THE PLAYER NEW CURRENT SCORE."""
        self._current_score = score

    def get_total_score(self):
        """GET THE PLAYER TOTAL SCORE."""
        return self._total_score

    def set_total_score(self, new_tscore):
        """SET THE PLAYER NEW TOTAL SCORE."""
        self._total_score = new_tscore

    def get_color(self):
        """GET THE PLAYER COLOR."""
        return self._color

    def set_color(self, new_color):
        """SETS THE PLAYERS CHOSEN COLOR."""
        new_color = str.lower(new_color)
        if (new_color in self.color_list):
            self._color = new_color
        else:
            raise ValueError("Enter on of the following colors: " +
                             "red, blue, green, magenta, yellow, cyan")

    def roll(self, dice: Dice):
        """
        PLAYER ROLL THE DICE

        IF THE OUTCOME IS 1 THE SCORE IS SET TO ZERO
        ELSE ADD THE OUTCOME TO CURRENT SCORE.
        """
        outcome = dice.roll_dice()
        if outcome == 1:
            self.set_score(0)
            self.change_turn()
        else:
            self.set_score(self.get_score() + outcome)

        return outcome

    def hold(self):
        """
        PLAYER HOLD

        PLAYER HOLD AND ADDS THE CURRENT SCORE TO THE TOTAL SCORE
        """
        self.set_total_score(self.get_score() + self.get_total_score())
