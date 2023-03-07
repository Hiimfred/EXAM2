"""Containst TestGame class."""
import unittest
from pig_game import game
from pig_game import player
from pig_game import intelligence
from pig_game import dice
from pig_game import highscore
from pig_game import difficulty


class TestGame(unittest.TestCase):
    """Methods that test the Game class."""

    def setUp(self):
        """Set up objects for testing."""
        self.curr_player = player.Player("P1", "blue")
        self.pend_player = player.Player("P2", "red")
        self.bot = intelligence.Intelligence()
        self.die = dice.Dice()
        self.highscore = highscore.Highscore()

    def test_game__init__(self):
    
    def test_new_difficulty(self):
        """Test new_difficulty method."""
        self.bot.set_difficulty(difficulty.Difficulty.HARD)
