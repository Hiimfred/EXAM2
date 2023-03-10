"""Contains Shell class."""
import cmd
from pyfiglet import figlet_format
from colorama import Fore
import game


class Shell(cmd.Cmd):
    """
    Shell class.

    Contains methods that responds to user input in the terminal.
    """

    titel = figlet_format("PIG GAME", font="isometric3")
    print(Fore.RED + titel)

    intro = "Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """Initiate the game object."""
        super().__init__()
        self.game = game.Game()

    def do_solo(self, arg):
        """
        Start a solo game, player vs bot.

        Takes one argument, the name of the player.
        """
        # Takes one argument and that is the players name.
        # If no argument is given then a message is printed.
        # Starts a solo game.
        # The prompt is set to the players name.

        msg = "\tOne argument required: Player1_name\n"
        if not arg:
            print(msg)
            return

        self.game.start_solo_game(arg)
        name_in_color = self.game.current_players_color() + arg
        self.prompt = f"({name_in_color + Fore.RED}) "

    def do_multiplayer(self, arg: str):
        """
        Start a multiplayer game, player vs player.

        Takes two arguments, the names of the two players.
        """
        # Takes two arguments, the names of the two players.
        # If no two arguments are given a message is printed.
        # Starts a multiplayer game.
        # The prompt is set to the first players name.

        args = arg.split()
        nr_args = len(args)

        if nr_args != 2:
            msg = "\tTwo arguments required: Player1_name Player2_name\n"
            print(msg)
            return

        self.game.start_multiplayer_game(args[0], args[1])
        name_in_color = self.game.current_players_color() + args[0]
        self.prompt = f"({name_in_color + Fore.RED}) "

    def do_roll(self, _):
        """
        If a game is running then roll the current players dice.

        Will pass the turn if a 1 is rolled and end the game if
        100 points is reached.
        """
        # If a 1 has been rolled then the player is informed
        # and depending on if it is a solo game or a multiplayer game
        # the bots turn is initiated or the turn is passed over to
        # the other player.
        # Else if the outcome was not a 1 then the game checks for a winner.
        # If no winner is found the outcome of the roll is printed.

        if not self.game.game_is_running():

            msg = "\tStart a game before you roll.\n"
            print(msg)
            return

        msg, outcome = self.game.roll()

        if outcome == 1:
            msg = "\tYou rolled a 1.. bummer!"
            print(msg)

            # This following part is basicly repeated in do_hold,
            # might be a good idea to make it into a method.
            if self.game.get_number_of_players() == 1:
                bot_msg = self.game.begin_bot_turn()
                print(bot_msg)
                self.check_for_winner()
            elif self.game.get_number_of_players() == 2:
                swap_msg = self.game.pass_turn()
                name = self.game.get_current_player_name()
                name_in_color = self.game.current_players_color() + name
                self.prompt = f"({name_in_color + Fore.RED}) "
                print(swap_msg)
        else:
            print(msg)
            self.check_for_winner()

    def do_hold(self, _):
        """
        If a game is running then hold the players points.

        The turn will also be passed over to the bot or the next player.
        Checks for winner. Ends game if winner is found.
        """
        if not self.game.game_is_running():
            msg = "\tStart a game before you hold.\n"
            print(msg)
            return

        hold_msg = self.game.hold()
        print(hold_msg)
        self.check_for_winner()

        if not self.game.is_winner():

            if self.game.get_number_of_players() == 1:
                bot_msg = self.game.begin_bot_turn()
                print(bot_msg)
                self.check_for_winner()
            elif self.game.get_number_of_players() == 2:
                swap_msg = self.game.pass_turn()
                name = self.game.get_current_player_name()
                name_in_color = self.game.current_players_color() + name
                self.prompt = f"({name_in_color + Fore.RED}) "
                print(swap_msg)

    def do_continue(self, _):
        """
        If there is a game to continue then reset the score and start over.

        You can choose to continue playing and collect wins for the highscore.
        """
        if (self.game.is_prior_game() and not self.game.game_is_running()):
            self.game.reset_game()
            msg = "\tThe game has been reset! You can now roll again.\n"
        else:
            msg = "\tThere is no game to continue. Finish a game first!\n"

        print(msg)

    def do_highscore(self, _):
        """Print the highscore list."""
        msg = self.game.display_highscore()
        print(msg)
        return ""

    def do_change_difficulty(self, _):
        """
        Change the difficulty of the bot.

        There is two settings EASY or HARD.
        """
        msg = self.game.new_difficulty()
        print(msg)

    def do_quit(self, _):
        """Save highscores and quits the game."""
        msg = "Thanks for playing!"
        print(msg)
        self.game.call_save_highscore()
        return True

    def do_cheat(self, _):
        """Set score to 99."""
        if not self.game.game_is_running():
            msg = "\tStart a game before you cheat.\n"
            print(msg)
            return
        msg = "You cheater.. your score is set to 99.."
        print(msg)
        self.game.activate_cheat()

    def do_color(self, arg):
        """
        Change player color to one of the following.

        Red, Blue, Green, Magenta, Yellow, Cyan.
        """
        if not self.game.game_is_running():
            msg = "\tStart a game before you change color.\n"
            print(msg)
            return
        if not arg:
            msg = "\tOne argument required: Color\n"
            print(msg)
            return
        try:
            self.game.change_color(arg)
            name = self.game.get_current_player_name()
            name_in_color = self.game.current_players_color() + name
            self.prompt = f"({name_in_color + Fore.RED}) "
        except ValueError as _ve:
            print(_ve)

    def check_for_winner(self):
        """
        Check if there is a winner to the game.

        If there is a winner then display it.
        """
        if self.game.is_winner():
            winner = self.game.get_winner()
            print(f"\t{winner.get_name()} won the game!!\n")
            self.game.end_game()
