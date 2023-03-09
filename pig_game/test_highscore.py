"""Contains TestHighscore class."""

import unittest
import player
import highscore


class TestHighscore(unittest.TestCase):
    """Methods that test the Highscore class."""

    def setUp(self):
        """Set up a Highscore object to test."""
        self.hs = highscore.Highscore()

    def test_highscore__init__(self):
        """Test highscore initiation."""
        self.assertFalse(self.hs._entries)

    def test_add_entry(self):
        """Test add_entry method."""
        p1 = player.Player("Test", "red")
        self.hs.add_entry(p1)

        length = len(self.hs._entries)
        self.assertEqual(length, 1)

        self.hs.add_entry(p1)
        self.assertEqual(length, 1)

    def test_not_empty(self):
        """Test not_empty method."""
        self.assertFalse(self.hs.not_empty())

        player1 = player.Player("Alice", "blue")
        self.hs.add_entry(player1)
        self.assertTrue(self.hs.not_empty())
