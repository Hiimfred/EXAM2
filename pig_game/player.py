"""CONTAINS A PLAYER CLASS"""
# Commented out stuff that caused errors, did not remove anything.
# from colorama import FORE, BACK, STYLE
from dice import Dice


class Player():
    """
    PLAYER CLASS

    CONTAINS GETTERS AND SETTERS FOR NAME, SCORE AND COLOR
    AND A CLASS MAKE_PLAY FOR THE PLAYER TO MAKE A MOVE IN THE GAME
    """
    # Removed this from _init_ arg ", color: FORE", caused error.
    def __init__(self, total_score: int, current_score: int, name: str, color: str):
        """
        DEFAULT PLAYER BLUEPRINT
        """

        self._total_score = 0
        self._current_score = 0
        self._name = name
        self._color = color

    def get_name(self):
        """
        GET THE PLAYER NAME
        """
        return self._name

    def set_name(self, new_name: str):
        """
        SET THE PLAYER NAME WHEN ENTERED
        """
        self._name = new_name

    def get_score(self):
        """
        GET THE PLAYER CURRENT SCORE
        """
        return self._current_score

    def get_total_score(self):
        """
        GET THE PLAYER TOTAL SCORE
        """
        return self._total_score

    def get_color(self):
        """
        GET THE PLAYER COLOR
        """
        return self._color

    def set_color(self, new_color):
        """
        SETS THE PLAYERS CHOSEN COLOR
        """
        self._color = new_color

    def make_play(self, dice: Dice):
        """
        PLAYER MAKE A MOVE TO ROLL DICE AND
        RUTURN OBTAINED SCORE
        """
        print("Rolling the dice... ")
        # result = Dice.roll_dice
        # current_score += result
        # return current_score
