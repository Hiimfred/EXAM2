"""Containst TestGame class."""
import unittest
from pig_game import game


class TestGame(unittest.TestCase):
    """Methods that test the Game class."""

    def setUp(self):
        """Set up objects for testing."""
        self.game = game.Game()

    def test_game__init__(self):
        ...

    def test_new_difficulty(self):
        """Test new_difficulty method."""
<<<<<<< HEAD
        self.game.start_solo_game("Player") 

    def test_set_number_of_players(self):
        self.assertRaises(ValueError, self.game.set_number_of_players, 3)
        self.assertRaises(ValueError, self.game.set_number_of_players, 0)
        self.assertRaises(ValueError, self.game.set_number_of_players, -1)
        self.game.set_number_of_players(1)
        self.assertEqual(self.game.get_number_of_players(), 1)
        self.game.set_number_of_players(2)
        self.assertEqual(self.game.get_number_of_players(), 2)
        ...
=======
        self.game.start_solo_game("Player")
        
>>>>>>> 62fb1169dbae4febcc3bafb1ac7220a5a1216835
