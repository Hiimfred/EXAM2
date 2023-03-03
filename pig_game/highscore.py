from player import Player
import pickle


class Highscore:
    ''''Construktor for keeping the score '''
    def __init__(self):
        self._entries = []

    def add_entry(self, player: Player):
        if (player not in self._entries):
            self._entries.append(player)
        else:
            player_index = self._entries.index(player)
            self._entries[player_index].set_nr_of_wins(player.get_nr_of_wins())

    def save_highscore(self):
        with open("highscore.bin", "wb") as file:
            pickle.dump(self._entries, file)

    def load_highscore(self):
        with open("highscore.bin", "rb") as file:
            self._entries = pickle.load(file)

    def get_highscore(self):
        highscore = ""
        for entry in self._entries:
            highscore += entry.__str__() + "\n"

        return highscore
