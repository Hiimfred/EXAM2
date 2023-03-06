"""Contains test for player class."""

import unittest
from pig_game import player


class test_player(unittest.TestCase):
    """METHOD THAT TESTS PLAYER METHODS."""

    def test_player__init__(self):
        """INITIATES PLAYER AND CHECK."""
        p1 = player.Player("Fred", "blue")

        self.assertEqual(p1.get_name(), "Fred")
        self.assertEqual(p1.get_color(), "blue")
        self.assertEqual(p1.get_total_score(), 0)
        self.assertEqual(p1.get_score(), 0)

    def test_set_name(self):
        """CHECK IF SET NAME IS CORRECT."""
        p1 = player.Player("Fred", "blue")

        p1.set_name("123@")
        self.assertEqual(p1.get_name(), "123@")

    def test_get_color(self):
        """..."""
        p1 = player.Player("Fred", "blue")

        self.assertEqual(p1.get_color(), "blue")

    def test_set_color(self):
        """..."""
        p1 = player.Player("Fred", "blue")

        p1.set_color("red")
        self.assertEqual(p1.get_color(), "red")
        self.assertRaises(ValueError, p1.set_color, "pink")
