"""Contains TestIntelligence class."""

import unittest
from pig_game import intelligence
from pig_game import difficulty


class TestIntelligence(unittest.TestCase):
    """Methods that test the Intelligence class."""

    def setUp(self):
        """Set up a default bot object."""
        self.bot = intelligence.Intelligence()

    def test_intelligence__init__(self):
        """Test initiation of Intelligence object."""
        self.assertEqual(self.bot._name, "Bot")
        self.assertEqual(self.bot._color, "red")
        self.assertEqual(self.bot._total_score, 0)
        self.assertEqual(self.bot._turn_score, 0)
        diff = self.bot._difficulty_setting
        self.assertTrue(diff is difficulty.Difficulty.EASY)

    def test_set_name(self):
        """Test the name value after using the set_name method."""
        self.bot.set_name("Test")
        self.assertEqual(self.bot._name, "Test")
        self.assertRaises(TypeError, self.bot.set_name, True)

    def test_get_name(self):
        """Test the get_name method."""
        self.bot._name = "Test2"
        self.assertEqual(self.bot.get_name(), "Test2")

    def test_set_turn_score(self):
        """Test the set_turn_score method."""
        self.bot.set_turn_score(10)
        self.assertEqual(self.bot._turn_score, 10)
        self.assertRaises(TypeError, self.bot.set_turn_score, "Str")

    def test_get_turn_score(self):
        """Test the get_turn_score method."""
        self.bot._turn_score = 20
        self.assertEqual(self.bot.get_turn_score(), 20)

    def test_set_total_score(self):
        """Test the set_total_score method."""
        self.bot.set_total_score(15)
        self.assertEqual(self.bot._total_score, 15)
        self.assertRaises(TypeError, self.test_set_total_score, "Str")

    def test_get_total_score(self):
        """Test the get_total_score method."""
        self.bot._total_score = 25
        self.assertEqual(self.bot.get_total_score(), 25)
