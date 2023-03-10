"""Unit testing."""
import unittest
from colorama import Fore
import player
import dice


class TestPlayer(unittest.TestCase):
    """Method that test player metod."""

    def test_player__init__(self):
        """
        Initiates player and check name and score.

        Test module to get name, color and score
        to give correct value.
        """
        player_test = player.Player("Fred", "blue")

        self.assertEqual(player_test.get_name(), "Fred")
        self.assertEqual(player_test.get_color(), Fore.BLUE)
        self.assertEqual(player_test.get_total_score(), 0)
        self.assertEqual(player_test.get_score(), 0)

    def test_get_name(self):
        """Check if get name is correct."""
        player_test = player.Player("Fred", "blue")

        player_test.set_name("Pelle")
        self.assertEqual(player_test.get_name(), "Pelle")

    def test_set_name(self):
        """Check if set name is correct."""
        player_test = player.Player("Fred", "blue")

        player_test.set_name("123@")
        self.assertEqual(player_test.get_name(), "123@")

    def test_get_color(self):
        """Check if player get correct set color."""
        player_test = player.Player("Fred", "blue")

        self.assertEqual(player_test.get_color(), Fore.BLUE)

    def test_set_color(self):
        """Check if player set color works as intended."""
        player_test = player.Player("Fred", "blue")

        player_test.set_color("red")
        self.assertEqual(player_test.get_color(), Fore.RED)
        self.assertRaises(ValueError, player_test.set_color, "pink")

    def test_roll(self):
        """
        Check if roll function works.

        Roll dice 10 times and checks outcome is is correct
        range (1-6) and that 1 adds no point and turn goes
        over to next player else cotinue to roll and add points
        each roll until 1 or hold.
        """
        player_test = player.Player("Fred", "blue")

        for _ in range(10):
            player_test.set_score(0)
            outcome = player_test.roll(dice.Dice())
            self.assertTrue(outcome >= 1 and outcome <= 6)
            if outcome == 1:
                self.assertEqual(player_test.get_score(), 0)
            else:
                self.assertEqual(player_test.get_score(), outcome)

    def test_hold(self):
        """Check if hold works and adds scoreto total score."""
        player_test = player.Player("Fred", "blue")

        player_test.set_total_score(0)
        player_test.set_score(50)
        player_test.hold()
        self.assertEqual(player_test.get_total_score(), 50)
        self.assertEqual(player_test.get_score(), 0)

    def test_add_win(self):
        """Check that wins add wins work properly."""
        player_test = player.Player("Fred", "blue")

        player_test.add_win()
        self.assertEqual(player_test.get_nr_of_wins(), 1)
        player_test.add_win()
        self.assertEqual(player_test.get_nr_of_wins(), 2)

    def test_get_nr_of_wins(self):
        """Check number of wins for player."""
        player_test = player.Player("Fred", "blue")

        player_test.set_nr_of_wins(5)
        self.assertEqual(player_test.get_nr_of_wins(), 5)
        player_test.set_nr_of_wins(10)
        self.assertEqual(player_test.get_nr_of_wins(), 10)

    def test_cheat(self):
        """Check if cheat works and give 99 points."""
        player_test = player.Player("Fred", "blue")

        player_test.cheat()
        self.assertEqual(player_test.get_total_score(), 99)
