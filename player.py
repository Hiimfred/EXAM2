"""Contains a player class."""
from dice import Dice


class Player():
    """
    Player class.

    Contains getter and setters for name, score, color Dan wins.
    Also contains methods for player to roll, hold and
    alter highscore numbers.
    """

    color_list = ["red", "blue", "green", "magenta", "yellow", "cyan"]

    def __init__(self, name: str, color: str):
        """Default player blueprint."""

        self._total_score = 0
        self._current_score = 0
        self._name = name
        self._color = color
        self._wins = 0

    def get_name(self):
        """Get the player name."""
        return self._name

    def set_name(self, new_name: str):
        """Set the player name when entered."""
        self._name = new_name

    def get_score(self):
        """Get the player current score."""
        return self._current_score

    def set_score(self, score):
        """Set the player new current score."""
        self._current_score = score

    def get_total_score(self):
        """Get the player total score."""
        return self._total_score

    def set_total_score(self, new_tscore):
        """Set the player new total score."""
        self._total_score = new_tscore

    def get_color(self):
        """Get the player color."""
        return self._color

    def set_color(self, new_color):
        """Set the player chosen color."""
        new_color = str.lower(new_color)
        if (new_color in self.color_list):
            self._color = new_color
        else:
            raise ValueError("Enter on of the following colors: " +
                             "red, blue, green, magenta, yellow, cyan")

    def add_win(self):
        """Add one win for player."""
        self._wins += 1

    def get_nr_of_wins(self):
        """Get number of wins for a player."""
        return self._wins

    def set_nr_of_wins(self, nr_wins: int):
        """Set number of wins for a player."""
        self._wins = nr_wins

    def roll(self, dice: Dice):
        """
        Player roll the dice.

        If the outcome is 1 the score is set to zero
        else add the outcome to current score.
        """
        outcome = dice.roll_dice()
        if outcome == 1:
            self.set_score(0)
        else:
            self.set_score(self.get_score() + outcome)

        return outcome

    def hold(self):
        """
        Player hold.

        Player hold and adds the current score to the total score.
        """
        self.set_total_score(self.get_score() + self.get_total_score())
        self.set_score(0)

    def __str__(self):
        """Return a formated string with name and number of wins."""
        return f"{self.get_name():^10} ---- {self.get_nr_of_wins():^10}"

    def cheat(self):
        """Cheat and set total score to 99."""
        self.set_total_score(99)
