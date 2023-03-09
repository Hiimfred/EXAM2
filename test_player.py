"""Unit testing."""

import unittest
import player
import dice
from colorama import Fore


class test_player(unittest.TestCase):
    """Method that test player metod."""

    def test_player__init__(self):
        """
        Initiates player and check name and score.

        Test module to get name, color and score
        to give correct value.
        """
        p1 = player.Player("Fred", "blue")

        self.assertEqual(p1.get_name(), "Fred")
        self.assertEqual(p1.get_color(), Fore.BLUE)
        self.assertEqual(p1.get_total_score(), 0)
        self.assertEqual(p1.get_score(), 0)

    def test_get_name(self):
        """Check if get name is correct."""
        p1 = player.Player("Fred", "blue")

        p1._name = "Pelle"
        self.assertEqual(p1.get_name(), "Pelle")

    def test_set_name(self):
        """Check if set name is correct."""
        p1 = player.Player("Fred", "blue")

        p1.set_name("123@")
        self.assertEqual(p1._name, "123@")

    def test_get_color(self):
        """Check if player get correct set color."""
        p1 = player.Player("Fred", "blue")

        self.assertEqual(p1.get_color(), Fore.BLUE)

    def test_set_color(self):
        """Check if player set color works as intended."""
        p1 = player.Player("Fred", "blue")

        p1.set_color("red")
        self.assertEqual(p1.get_color(), Fore.RED)
        self.assertRaises(ValueError, p1.set_color, "pink")

    def test_roll(self):
        """
        Check if roll function works.

        Roll dice 10 times and checks outcome is is correct 
        range (1-6) and that 1 adds no point and turn goes
        over to next player else cotinue to roll and add points
        each roll until 1 or hold.
        """
        p1 = player.Player("Fred", "blue")

        for i in range(10):
            p1.set_score(0)
            outcome = p1.roll(dice.Dice())
            self.assertTrue(outcome >= 1 and outcome <= 6)
            if outcome == 1:
                self.assertEqual(p1.get_score(), 0)
            else:
                self.assertEqual(p1.get_score(), outcome)

    def test_hold(self):
        """
        Check if hold works and adds score
        to total score.
        """
        p1 = player.Player("Fred", "blue")

        p1.set_total_score(0)
        p1.set_score(50)
        p1.hold()
        self.assertEqual(p1.get_total_score(), 50)
        self.assertEqual(p1.get_score(), 0)

    def test_add_win(self):
        """Check that wins add wins work properly."""
        p1 = player.Player("Fred", "blue")

        p1.add_win()
        self.assertEqual(p1.get_nr_of_wins(), 1)
        p1.add_win()
        self.assertEqual(p1.get_nr_of_wins(), 2)

    def test_get_nr_of_wins(self):
        """Check number of wins for player."""
        p1 = player.Player("Fred", "blue")

        p1.set_nr_of_wins(5)
        self.assertEqual(p1.get_nr_of_wins(), 5)
        p1.set_nr_of_wins(10)
        self.assertEqual(p1.get_nr_of_wins(), 10)

    def test_cheat(self):
        """Check if cheat works and give 99 points."""
        p1 = player.Player("Fred", "blue")

        p1.cheat()
        self.assertEqual(p1.get_total_score(), 99)
