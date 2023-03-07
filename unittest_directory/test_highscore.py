import unittest
from pig_game import player
from pig_game import highscore


class TestHighscore(unittest.TestCase):
    def setUp(self):
        self.hs = highscore.Highscore()

    def test_add_entry(self):
        player1 = player.Player("Alice", "red")
        player2 = player.Player("Bob", "blue")
        player3 = player.Player("Charlie", "cyan")

        '''Add player1 to empty highscore'''
        self.hs.add_entry(player1)
        self.assertEqual(self.hs._entries, [player1])

        '''Add player2 to non-empty highscore'''
        self.hs.add_entry(player2)
        self.assertEqual(self.hs._entries, [player1, player2])

        '''Add player1 again with more wins'''
        player1.set_nr_of_wins(3)
        self.hs.add_entry(player1)
        self.assertEqual(self.hs._entries, [player1, player2])

        '''Add player3 with more wins than existing players'''
        player3.set_nr_of_wins(5)
        self.hs.add_entry(player3)
        self.assertEqual(self.hs._entries, [player3, player1, player2])

    def test_save_load_highscore(self):
        player1 = player.Player("Alice", "red")
        player2 = player.Player("Bob", "blue")

        self.hs.add_entry(player1)
        self.hs.add_entry(player2)

        ''' Save and load highscore '''
        self.hs.save_highscore()
        self.hs._entries = []
        self.hs.load_highscore()
        self.assertEqual(self.hs._entries, [player1, player2])

    def test_get_highscore(self):
        player1 = player.Player("Alice", "red")
        player2 = player.Player("Bob", "blue")

        self.hs.add_entry(player1)
        self.hs.add_entry(player2)

        expected_output = "   Name    ----    Wins   \n"
        expected_output += "  Alice    ----      1    \n"
        expected_output += "   Bob     ----      1    \n"

        self.assertEqual(self.hs.get_highscore(), expected_output)

    def test_not_empty(self):
        '''Empty highscore'''
        self.assertFalse(self.hs.not_empty())

        '''Non-empty highscore'''
        player1 = player.Player("Alice", "red")
        self.hs.add_entry(player1)
        self.assertTrue(self.hs.not_empty())
