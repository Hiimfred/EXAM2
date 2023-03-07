"""Contains test for player class."""

import unittest
from pig_game import player
from pig_game import dice


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
        self.assertEqual(p1.get_color(), "blue")
        self.assertEqual(p1.get_total_score(), 0)
        self.assertEqual(p1.get_score(), 0)

    def test_set_name(self):
        """Check if set name is correct."""
        p1 = player.Player("Fred", "blue")

        p1.set_name("123@")
        self.assertEqual(p1.get_name(), "123@")

    def test_get_color(self):
        """Check if player get correct set color."""
        p1 = player.Player("Fred", "blue")

        self.assertEqual(p1.get_color(), "blue")

    def test_set_color(self):
        """Check if player set color works as intended."""
        p1 = player.Player("Fred", "blue")

        p1.set_color("red")
        self.assertEqual(p1.get_color(), "red")
        self.assertRaises(ValueError, p1.set_color, "pink")
    
    def test_roll(self):
        p1 = player.Player("Fred","blue")
        
        for i in range(10):
            p1.set_score(0)
            outcome = p1.roll(dice.Dice())
            self.assertTrue(outcome >= 1 and outcome <= 6)
            if outcome == 1:
                self.assertEqual(p1.get_score(), 0)
            else:
                self.assertEqual(p1.get_score(),outcome)
    
    def test_hold(self):
        p1 = player.Player("Fred", "blue")
        
        p1.set_total_score(0)
        p1.set_score(50)
        p1.hold()
        self.assertEqual(p1.get_total_score(), 50)
        self.assertEqual(p1.get_score(), 0)
        
        