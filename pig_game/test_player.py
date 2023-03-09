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
        test_player = player.Player("Fred", "blue")

        self.assertEqual(test_player.get_name(), "Fred")
        self.assertEqual(test_player.get_color(), Fore.BLUE)
        self.assertEqual(test_player.get_total_score(), 0)
        self.assertEqual(test_player.get_score(), 0)

    def test_get_name(self):
        """Check if get name is correct."""
        test_player = player.Player("Fred", "blue")

        test_player._name = "Pelle"
        self.assertEqual(test_player.get_name(), "Pelle")

    def test_set_name(self):
        """Check if set name is correct."""
        test_player = player.Player("Fred", "blue")

        test_player.set_name("123@")
        self.assertEqual(test_player._name, "123@")

    def test_get_color(self):
        """Check if player get correct set color."""
        test_player = player.Player("Fred", "blue")

        self.assertEqual(test_player.get_color(), Fore.BLUE)

    def test_set_color(self):
        """Check if player set color works as intended."""
        test_player = player.Player("Fred", "blue")

        test_player.set_color("red")
        self.assertEqual(test_player.get_color(), Fore.RED)
        self.assertRaises(ValueError, test_player.set_color, "pink")

    def test_roll(self):
        """
        Check if roll function works.

        Roll dice 10 times and checks outcome is is correct
        range (1-6) and that 1 adds no point and turn goes
        over to next player else cotinue to roll and add points
        each roll until 1 or hold.
        """
        test_player = player.Player("Fred", "blue")

        for i in range(10):
            test_player.set_score(0)
            outcome = test_player.roll(dice.Dice())
            self.assertTrue(outcome >= 1 and outcome <= 6)
            if outcome == 1:
                self.assertEqual(test_player.get_score(), 0)
            else:
                self.assertEqual(test_player.get_score(), outcome)

    def test_hold(self):
        """Check if hold works and adds scoreto total score."""
        test_player = player.Player("Fred", "blue")

        test_player.set_total_score(0)
        test_player.set_score(50)
        test_player.hold()
        self.assertEqual(test_player.get_total_score(), 50)
        self.assertEqual(test_player.get_score(), 0)

    def test_add_win(self):
        """Check that wins add wins work properly."""
        test_player = player.Player("Fred", "blue")

        test_player.add_win()
        self.assertEqual(test_player.get_nr_of_wins(), 1)
        test_player.add_win()
        self.assertEqual(test_player.get_nr_of_wins(), 2)

    def test_get_nr_of_wins(self):
        """Check number of wins for player."""
        test_player = player.Player("Fred", "blue")

        test_player.set_nr_of_wins(5)
        self.assertEqual(test_player.get_nr_of_wins(), 5)
        test_player.set_nr_of_wins(10)
        self.assertEqual(test_player.get_nr_of_wins(), 10)

    def test_cheat(self):
        """Check if cheat works and give 99 points."""
        test_player = player.Player("Fred", "blue")

        test_player.cheat()
        self.assertEqual(test_player.get_total_score(), 99)
