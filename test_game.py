import unittest
import game
import player


class TestGame(unittest.TestCase):
    """Methods that test the Game class."""

    def setUp(self):
        """Set up objects for testing."""
        self.p1 = player.Player("bob", "blue")
        self.game = game.Game()

    def test_game__init__(self):
        """Test initiation of game."""
        self.assertEqual(self.game._score_to_win, 100)
        self.assertEqual(self.game._number_of_players, "Not set")
        self.assertEqual(self.game._text_color, "magenta")
        self.assertIsNotNone(self.game._die)
        self.assertIsNotNone(self.game._highscore)

    def test_set_number_of_players(self):
        """
        Test that it works with 1-2 player and it can't
        be played with less or more.
        """
        self.assertRaises(ValueError, self.game.set_number_of_players, 3)
        self.assertRaises(ValueError, self.game.set_number_of_players, 0)
        self.assertRaises(ValueError, self.game.set_number_of_players, -1)
        self.game.set_number_of_players(1)
        self.assertEqual(self.game.get_number_of_players(), 1)
        self.game.set_number_of_players(2)
        self.assertEqual(self.game.get_number_of_players(), 2)

    def test_set_score_to_win(self):
        """Test if set score to win works properly."""
        self.game.set_score_to_win(100)
        self.assertEqual(self.game.get_score_to_win(), 100)

        self.game.set_score_to_win(50)
        self.assertEqual(self.game.get_score_to_win(), 50)

    def test_multiplayer_game(self):
        """Test to start a multiplayer game."""
        name1 = "p1"
        name2 = "p2"

        self.game.start_multiplayer_game(name1, name2)
        self.assertTrue(self.game.game_is_running())
        self.assertEqual(self.game._number_of_players, 2)
        self.assertIsNotNone(self.game._current_player)
        self.assertIsNotNone(self.game._pending_player)
        self.assertEqual(self.game._current_player.get_name(), name1)
        self.assertEqual(self.game._pending_player.get_name(), name2)
        self.assertEqual(self.game._current_player.get_color(), "blue")
        self.assertEqual(self.game._pending_player.get_color(), "red")

    def test_game_is_running(self):
        """Test that game run and ends correctly."""
        self.assertFalse(self.game.game_is_running())
        self.game.start_solo_game(self.p1)
        self.assertTrue(self.game.game_is_running())
        self.game.end_game()
        self.assertFalse(self.game.game_is_running())

    def test_activate_cheat(self):
        """
        Test activate cheat to see it adds 99 point
        to current player.
        """
        self.game.start_solo_game(self.p1)

        start_score = self.game._current_player.get_total_score()
        self.game.activate_cheat()
        new_score = self.game._current_player.get_total_score()
        self.assertEqual(new_score, 99)
        self.assertNotEqual(start_score, new_score)
