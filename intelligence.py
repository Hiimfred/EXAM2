"""Contains Intelligence class."""
from dice import Dice
from difficulty import Difficulty
from player import Player
from game import Game


class Intelligence:
    """
    Intelligence class.

    Contains variables and methods regarding the NPC and its behaviour.
    """

    def __init__(self, name: str, color):
        """Initiate a default Intelligence object with a name and a color."""
        self._total_score = 0
        self._turn_score = 0
        self._difficulty_setting = Difficulty.HARD
        self._name = name
        # Not sure how to handle the color picking yet.
        self._color = color
        # Here a method that somehow uses the choosen color
        # when the NPC´s name is displayed needs to be inserted.

    def set_name(self, name: str):
        """Set a new name for this Intelligence object."""
        self._name = name

    def get_name(self):
        """Return the name of this Intelligence object."""
        return self._name

    def get_score(self):
        """Return the current score for this Intelligence object."""
        return self._turn_score

    def get_total_score(self):
        """Return the total score for this Intelligence object."""
        return self._total_score

    def set_color(self, color):
        """Set a new color for this Intelligence object."""
        self._color = color

    def get_color(self):
        """Return the color of this Intelligence object."""
        return self._color

    def set_difficulty(self, difficulty: int):
        """
        Apply a new difficulty setting to this Intelligence object.

        If the argument is not in the correct range a ValueError is raised.
        """
        if (difficulty > 0 and difficulty < 3):
            # Not sure that this will work as intended.
            # Trying to set the diffculty_setting acording
            # to the input number.
            self._difficulty_setting = Difficulty(difficulty)
        else:
            raise ValueError("Difficulty value needs to be integer 1 or 2.")

    def make_play(self, dice: Dice, player_opponent: Player, game: Game):
        """Initiate the NPCs turn."""
        _rolls_this_turn = 0
        self._turn_score = 0
        _run = True

        if (self._difficulty_setting is Difficulty.EASY):
            while (self._total_score < 100 and _rolls_this_turn < 6 and _run):

                outcome_e = dice.roll_dice()
                _rolls_this_turn += 1

                if (outcome_e != 1):
                    print(f"{self._name} rolled a {outcome_e}..")
                    self._turn_score += outcome_e
                else:
                    self._turn_score = 0
                    _run = False
        elif (self._difficulty_setting is Difficulty.HARD):
            # Variables to shorten the length of if-statements.
            s = dice.get_number_of_sides()
            w = game.get_score_to_win()
            o = player_opponent.get_total_score()
            p = self.get_total_score()

            while (self._total_score < 100 and _run):

                outcome_h = dice.roll_dice()
                _rolls_this_turn += 1

                # Change inside of if statements to show how many
                # times to loop and then put while-loop after.
                if (outcome_h == 1):
                    self._turn_score = 0
                    _run = False
                elif (p == 0 and outcome_h >= round(s * 0.6)):
                    self._turn_score += outcome_h
                    _run = False
                elif (o > round(w * 0.5) and (o - p) >= round(w * 0.2)):
                    self._turn_score += outcome_h
                    if (_rolls_this_turn > 3):
                        _run = False
                elif (p - o) >= round(w * 0.3):
                    self._turn_score += outcome_h
                    if (_rolls_this_turn >= 2):
                        _run = False
                elif (o > (w * 0.4) and (o - p) <= round(w * 0.9)):
                    self._turn_score += outcome_h
                    _run = False
                elif (o - p) >= round(w * 0.8) and o >= round(w * 0.8):
                    self._turn_score += outcome_h

        self._total_score += self._turn_score
