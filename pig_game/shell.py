"""Contains Shell class."""
import cmd
import game
from player import Player
from intelligence import Intelligence


class Shell(cmd.Cmd):
    """
    Shell class.

    Contains methods that responds to user input in the terminal.
    """

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, arg1, arg2):
        nr_args = len(self.args)
        err_msg = "There needs to be atleast one player."

        if (nr_args < 1 or nr_args > 2):
            print(err_msg)
            return
        elif (nr_args == 1):
            self.Player1 = Player(arg1, "blue")
            self.NPC = Intelligence()
        else:
            self.Player1 = Player(arg1, "blue")
            self.Player2 = Player(arg2, "red")
