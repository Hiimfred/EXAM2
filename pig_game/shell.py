"""Contains Shell class."""
import cmd
import game


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

        err_msg = "There needs to be atleast one player."
        if (not arg1):
            print(err_msg)
            return
        elif (not arg2):
            ...