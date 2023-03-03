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
            self.prompt = f"({arg}) "

    def do_multiplayer(self, arg: str):
        args = arg.split()
        nr_args = len(args)

        if (nr_args != 2):
            msg = "Two arguments required: Player1_name Player2_name"
            print(msg)
            return
        else:
            self.game.start_multiplayer_game(args[0], args[1])
            self.prompt = f"({args[0]})"

    def do_roll(self, _):

        if (not self.game.game_is_running()):
            msg = "\tStart a game before you roll.\n"
            print(msg)
            return

        msg, outcome = self.game.roll()

        if (outcome == 1):
            msg = "\tYou rolled a 1.. bummer!"
            print(msg)

            if (self.game.get_number_of_players() == 1):
                bot_msg = self.game.begin_bot_turn()
                print(bot_msg)
            elif (self.game.get_number_of_players() == 2):
                swap_msg = self.game.pass_turn()
                self.prompt = f"({self.game.get_current_player_name()}) "
                print(swap_msg)
        else:

            if (self.game.is_winner()):
                winner = self.game.get_winner()
                print(f"\t{winner.get_name()} won the game!!")
                self.game.end_game()
                self.game.reset_game()
            else:
                print(msg)

    def do_hold(self, _):

        if (not self.game.game_is_running()):
            msg = "\tStart a game before you hold.\n"
            print(msg)
            return

        hold_msg = self.game.hold()
        print(hold_msg)

        if (self.game.get_number_of_players() == 1):
            bot_msg = self.game.begin_bot_turn()
            print(bot_msg)

            if (self.game.is_winner()):
                winner = self.game.get_winner()
                print(f"\t{winner.get_name()} won the game!!")
                self.game.end_game()
                self.game.reset_game()
        else:
            swap_msg = self.game.pass_turn()
            self.prompt = f"({self.game.get_current_player_name()}) "
            print(swap_msg)

    def do_continue(self, _):
        if (self.game.is_prior_game() and not self.game.game_is_running()):
            self.game.reset_game()
            msg = "\n\tThe game has been reset! You can now roll again."
        else:
            msg = "\n\tThere is no game to continue. Finish a game first!"

        print(msg)
