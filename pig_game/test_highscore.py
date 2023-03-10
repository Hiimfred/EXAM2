"""Contains TestHighscore class."""

import unittest
import player
import highscore


class TestHighscore(unittest.TestCase):
    """Methods that test the Highscore class."""

    def setUp(self):
        """Set up a Highscore object to test."""
        self._hs = highscore.Highscore()

    def test_highscore__init__(self):
        """Test highscore initiation."""
        self.assertFalse(self._hs.get_entries())

    def test_add_entry(self):
        """Test add_entry method."""
        test_player = player.Player("Test", "red")
        self._hs.add_entry(test_player)

        length = len(self._hs.get_entries())
        self.assertEqual(length, 1)

        self._hs.add_entry(test_player)
        self.assertEqual(length, 1)

    def test_not_empty(self):
        """Test not_empty method."""
        self.assertFalse(self._hs.not_empty())

        test_player = player.Player("Alice", "blue")
        self._hs.add_entry(test_player)
        self.assertTrue(self._hs.not_empty())
