"""Contains TestIntelligence class."""

import unittest
import intelligence
import difficulty
import player


class TestIntelligence(unittest.TestCase):
    """Methods that test the Intelligence class."""

    def setUp(self):
        """Set up a default bot object."""
        self.bot = intelligence.Intelligence()

    def test_intelligence__init__(self):
        """Test initiation of Intelligence object."""
        self.assertEqual(self.bot.get_name(), "Bot")
        self.assertEqual(self.bot._color, "red")
        self.assertEqual(self.bot.get_total_score(), 0)
        self.assertEqual(self.bot.get_turn_score(), 0)
        diff = self.bot.get_difficulty()
        self.assertTrue(diff is difficulty.Difficulty.EASY)

    def test_set_name(self):
        """Test the name value after using the set_name method."""
        self.bot.set_name("Test")
        self.assertEqual(self.bot.get_name(), "Test")
        self.assertRaises(TypeError, self.bot.set_name, True)

    def test_get_name(self):
        """Test the get_name method."""
        self.bot.set_name("Test2")
        self.assertEqual(self.bot.get_name(), "Test2")

    def test_set_turn_score(self):
        """Test the set_turn_score method."""
        self.bot.set_turn_score(10)
        self.assertEqual(self.bot.get_turn_score(), 10)
        self.assertRaises(TypeError, self.bot.set_turn_score, "Str")

    def test_get_turn_score(self):
        """Test the get_turn_score method."""
        self.bot.set_turn_score(20)
        self.assertEqual(self.bot.get_turn_score(), 20)

    def test_set_total_score(self):
        """Test the set_total_score method."""
        self.bot.set_total_score(15)
        self.assertEqual(self.bot.get_total_score(), 15)
        self.assertRaises(TypeError, self.test_set_total_score, "Str")

    def test_get_total_score(self):
        """Test the get_total_score method."""
        self.bot.set_total_score(25)
        self.assertEqual(self.bot.get_total_score(), 25)

    def test_set_color(self):
        """Test the set_color method."""
        self.bot.set_color("green")
        self.assertEqual(self.bot._color, "green")
        self.assertRaises(TypeError, self.bot.set_color, True)

    def test_get_color(self):
        """Test the get_color method."""
        self.bot._color = "red"
        self.assertEqual(self.bot.get_color(), "red")

    def test_set_difficulty(self):
        """Test the set_difficulty method."""
        self.bot.set_difficulty(difficulty.Difficulty.HARD)
        diff = self.bot.get_difficulty()
        self.assertTrue(diff is difficulty.Difficulty.HARD)

    def test_get_difficulty(self):
        """Test the get_difficulty method."""
        self.bot.set_difficulty(difficulty.Difficulty.EASY)
        self.assertEqual(self.bot.get_difficulty(), difficulty.Difficulty.EASY)

    def test_make_play(self):
        """Test the make_play method."""
        test_player = player.Player("Robert", "blue")
        self.bot.set_difficulty(difficulty.Difficulty.EASY)
        for _ in range(5):
            outcomes = self.bot.make_play(test_player)
            length = len(outcomes)
            self.assertTrue(length >= 1 or length <= 2)

        self.bot.set_difficulty(difficulty.Difficulty.HARD)
        test_player.set_total_score(81)
        self.bot.set_total_score(71)
        for _ in range(10):
            outcomes = self.bot.make_play(test_player)
            length = len(outcomes)
            self.assertTrue(length >= 1 or length <= 9)

        test_player.set_total_score(61)
        for _ in range(10):
            outcomes = self.bot.make_play(test_player)
            length = len(outcomes)
            self.assertTrue(length >= 1 or length <= 4)

        self.bot.set_total_score(40)
        test_player.set_total_score(40)
        for _ in range(10):
            outcomes = self.bot.make_play(test_player)
            length = len(outcomes)
            self.assertTrue(length >= 1 or length <= 3)
