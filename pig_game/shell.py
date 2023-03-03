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

    def do_solo(self, arg):
        msg = "One argument required: Player1 name"
        if not arg:
            print(msg)
            return
        else:
            self.game.start_solo_game(arg)

    def do_multiplayer(self, arg1, arg2):
        msg = "Two arguments required: Player1 and Player2 names"
        args = len(self.args)

        if (args != 2):
            print(msg)
            return
        else:
            self.game.start_multiplayer_game(arg1, arg2)

    def do_roll(self):
        msg = self.game.roll()
        print(msg)

    def do_hold(self):
        hold_msg = self.game.hold()
        print(hold_msg)

        if (self.game.check_for_winner()):
            winner = self.game.get_winner()
            print(f"{winner.get_name()} won the game!!")

        if (self.game.get_number_of_players() == 1):
            bot_msg = self.game.begin_bot_turn()
            print(bot_msg)

            if (self.game.check_for_winner()):
                winner = self.game.get_winner()
                print(f"{winner.get_name()} won the game!!")
        else:
            swap_msg = self.game.pass_turn()
            print(swap_msg)
