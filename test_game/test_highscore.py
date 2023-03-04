from pig_game.highscore import Highscore
import unittest

class TestHighscore(unittest.TestCase):
    
    def test_initial_scores(self):
        """
        Test if the initial scores for both the player and the bot are zero.
        """
        highscore = Highscore("Player1")
        self.assertEqual(highscore.getplayer_score(), 0)
        self.assertEqual(highscore.getbot_score(), 0)

    def test_set_scores(self):
        """
        Test if the player and bot scores are set correctly.
        """
        highscore = Highscore("Player2")
        highscore.setPlayer_score(10)
        highscore.setBot_score(5)
        self.assertEqual(highscore.getplayer_score(), 10)
        self.assertEqual(highscore.getbot_score(), 5)

    def test_print_scoreboard(self):
        """
        Test if the scoreboard is printed correctly.
        """
        highscore = Highscore("Player3")
        highscore.setPlayer_score(20)
        highscore.setBot_score(15)
        expected_output = "Scoreboard for Player3\nPlayer3: 20\nBot: 15\n"
        self.assertEqual(highscore.print_scoreboard(), expected_output)