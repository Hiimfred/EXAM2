"""Contains TestDice class."""

import unittest
import dice


class TestDice(unittest.TestCase):
    """Methods that test dice functionality."""

    def test_dice__init__(self):
        """Initiates dice and checks that values are correct."""
        die = dice.Dice()

        self.assertEqual(die.get_side_up(), 1)
        self.assertEqual(die.get_number_of_sides(), 6)

    def test_set_side_value(self):
        """Raise value error when needed."""
        die = dice.Dice()

        self.assertRaises(ValueError, die.set_number_of_sides, -1)

    def test_set_side_type(self):
        """Raise type error when needed."""
        die = dice.Dice()

        self.assertRaises(TypeError, die.set_number_of_sides, True)
        self.assertRaises(TypeError, die.set_number_of_sides, "String")

    def test_dice_roll(self):
        """Check if dice roll values are within the correct bounds."""
        die = dice.Dice()
        nr_sides = die.get_number_of_sides()

        for i in range(10):
            out = die.roll_dice()
            self.assertTrue(out >= 1 and out <= nr_sides)

    def test_get_side_up(self):
        """Check if the value returned is the expected value."""
        die = dice.Dice()

        die.set_number_of_sides(2)
        self.assertEqual(die.get_number_of_sides(), 2)
