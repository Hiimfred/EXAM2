"""Contains Highscore class."""
import pickle
from player import Player


class Highscore:
    """
    Highscore class.

    Cointains methods and variables that related to the highscore.
    """

    def __init__(self):
        """Initialize the entries list."""
        self._entries = []

    def add_entry(self, player: Player):
        """Add player to the highscore list or update their number of wins."""
        if player not in self._entries:
            self._entries.append(player)
        else:
            player_index = self._entries.index(player)
            self._entries[player_index].set_nr_of_wins(player.get_nr_of_wins())

    def save_highscore(self):
        """Save the highscore list to a file using pickle."""
        with open("pig_game/highscore.bin", "wb") as file:
            pickle.dump(self._entries, file)

    def load_highscore(self):
        """Load the highscore list from a file using pickle."""
        try:
            with open("pig_game/highscore.bin", "rb") as file:
                self._entries = pickle.load(file)
        except EOFError:
            ...

    def get_highscore(self):
        """Get the highscore list as a formatted string."""
        highscore = f"{'Name':^10} ---- {'Wins':^10}\n"
        for entry in self._entries:
            highscore += str(entry) + "\n"

        return highscore

    def not_empty(self):
        """Check if the highscore list is not empty."""
        if self._entries:
            return True
        return False

    def get_entries(self):
        """Return the entries."""
        return self._entries
