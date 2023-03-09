"""Contains TestGame class."""
import unittest
import game
import player
import difficulty


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
        """Test that set_number_of_players works with 1 or 2 players."""
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

    def test_is_winner(self):
        """Test the is_winner method."""
        self.game._current_player = player.Player("Test_name", "red")
        self.game.set_number_of_players(1)

        self.assertFalse(self.game.is_winner())
        self.game._bot.set_total_score(100)
        self.assertTrue(self.game.is_winner())

    def test_get_current_player_name(self):
        """Test the get_current_player_name method."""
        self.game._current_player = player.Player("Test_name", "cyan")
        self.assertEqual(self.game.get_current_player_name(), "Test_name")

    def test_end_game(self):
        """Test the end_game method."""
        self.game._game_started = True
        self.game._prior_game = False

        self.game.end_game()

        self.assertFalse(self.game._game_started)
        self.assertTrue(self.game._prior_game)

    def test_is_prior_game(self):
        """Test is_prior_game method."""
        self.assertFalse(self.game.is_prior_game())
        self.game._prior_game = True
        self.assertTrue(self.game.is_prior_game())

    def test_reset_game(self):
        """Test reset_game method."""
        self.game._current_player = player.Player("Test_name", "red")
        self.game._pending_player = player.Player("Test_name2", "blue")
        self.game._current_player.set_total_score(100)
        self.game._pending_player.set_total_score(100)
        self.game._bot.set_total_score(100)
        self.game._game_started = False

        self.game.set_number_of_players(1)
        self.game.reset_game()
        self.game.set_number_of_players(2)
        self.game.reset_game()
        self.assertEqual(self.game._current_player.get_total_score(), 0)
        self.assertEqual(self.game._pending_player.get_total_score(), 0)
        self.assertEqual(self.game._bot.get_total_score(), 0)
        self.assertTrue(self.game._game_started)

    def test_game_is_running(self):
        """Test that game run and ends correctly."""
        self.assertFalse(self.game.game_is_running())
        self.game.start_solo_game(self.p1)
        self.assertTrue(self.game.game_is_running())
        self.game.end_game()
        self.assertFalse(self.game.game_is_running())

    def test_activate_cheat(self):
        """Test activate_cheat to see that it adds 99 point."""
        self.game.start_solo_game(self.p1)

        start_score = self.game._current_player.get_total_score()
        self.game.activate_cheat()
        new_score = self.game._current_player.get_total_score()
        self.assertEqual(new_score, 99)
        self.assertNotEqual(start_score, new_score)

    def test_display_highscore(self):
        """Test display_highscore method."""
        self.game._highscore._entries = []
        msg = self.game.display_highscore()
        self.assertEqual(msg, "\tThere are no highscores.\n")

    def test_new_difficulty(self):
        """Test new_difficulty method."""
        diff = self.game._bot.get_difficulty()
        self.assertEqual(diff, difficulty.Difficulty.EASY)
        msg = self.game.new_difficulty()
        self.assertEqual(msg, "\tBot difficulty set to HARD.\n")
        diff = self.game._bot.get_difficulty()
        self.assertEqual(diff, difficulty.Difficulty.HARD)
