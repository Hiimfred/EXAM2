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
        test_player = player.Player("Test", "red")
        self.hs.add_entry(test_player)

        length = len(self.hs._entries)
        self.assertEqual(length, 1)

        self.hs.add_entry(test_player)
        self.assertEqual(length, 1)

    def test_not_empty(self):
        """Test not_empty method."""
        self.assertFalse(self.hs.not_empty())

        test_player = player.Player("Alice", "blue")
        self.hs.add_entry(test_player)
        self.assertTrue(self.hs.not_empty())
