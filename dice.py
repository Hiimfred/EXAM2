"""Contains Dice class."""
import random


class Dice:
    """
    Dice class.

    Contains methods for creating a manitpulating the games dice.
    """

    def __init__(self):
        """
        Initiate a default dice.

        Default dice with 6 sides and 1 facing upwards.
        """
        self.side_up = 1
        self.number_of_sides = 6

    def set_number_of_sides(self, number_of_sides: int):
        """
        Set the number of sides on the dice.

        Check if the input is valid.
        If it is then set the number of sides on the dice.
        Otherwise display message.
        """
        if (number_of_sides > 1):
            self.number_of_sides = number_of_sides
        else:
            print("Invalid input. Positive integer larger than 1 required.")

    def roll_dice(self):
        """
        Roll dice return the outcome.

        Generates random number between 1 and the number_of_sides on the dice.
        Changes the side up and returns the outcome of the roll.
        """
        outcome = random.randint(1, self.number_of_sides)
        self.side_up = outcome

        return outcome
