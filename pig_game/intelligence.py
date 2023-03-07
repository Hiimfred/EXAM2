"""Contains Intelligence class."""
from .dice import Dice
from .difficulty import Difficulty
from .player import Player


class Intelligence:
    """
    Intelligence class.

    Contains variables and methods regarding the NPC and its behaviour.
    """

    _die = Dice()
    _total_score = 0
    _turn_score = 0
    _difficulty_setting = Difficulty.EASY

    def __init__(self):
        """Initiate a default Intelligence object with a name and a color."""
        self._name = "Bot"
        self._color = "red"

    def set_name(self, name: str):
        """Set a new name for this Intelligence object."""
        if (isinstance(name, str)):
            self._name = name
        else:
            raise TypeError("Name must be a string.")

    def get_name(self):
        """Return the name of this Intelligence object."""
        return self._name

    def set_turn_score(self, score: int):
        """Set the score for this round for this Intelligence object."""
        if (isinstance(score, int)):
            self._turn_score = score
        else:
            raise TypeError("Must be an integer.")

    def get_turn_score(self):
        """Return the current score for this Intelligence object."""
        return self._turn_score

    def set_total_score(self, total_score: int):
        """Set the total score for this Intelligence object."""
        if (isinstance(total_score, int)):
            self._total_score = total_score
        else:
            raise TypeError("Must be an integer.")

    def get_total_score(self):
        """Return the total score for this Intelligence object."""
        return self._total_score

    def set_color(self, color: str):
        """Set a new color for this Intelligence object."""
        self._color = color

    def get_color(self):
        """Return the color of this Intelligence object."""
        return self._color

    def set_difficulty(self, difficulty: Difficulty):
        """Apply a new difficulty setting to this Intelligence object."""
        self._difficulty_setting = difficulty

    def get_difficulty(self):
        """Return the difficulty setting of the Intelligence object."""
        return self._difficulty_setting

    def make_play(self, player: Player):
        """
        Initiate the NPCs turn.

        There is two difficulty settings, EASY and HARD.
        The npc set to EASY will always throw two times
        while the NPC set to HARD will try to adapt
        its playstyle depending on factors like:
        Oponents score, the NPCs score,
        how many points there are left until someone wins
        and who is in the lead.
        """
        _rolls_this_turn = 0
        self._turn_score = 0
        _run = True
        throws = "Not set"
        score_left = "Not set"

        # This is variables to make the if-statements
        # (Starting at line 96) shorter and more readable.
        op_score = player.get_total_score()
        npc_score = self.get_total_score()
        op_lead = player.get_total_score() - self.get_total_score()
        npc_lead = self.get_total_score() - player.get_total_score()
        if (op_score > npc_score):
            score_left = 100 - op_score
        else:
            score_left = 100 - npc_score

        # The EASY NPC always throws 2 times.
        if (self._difficulty_setting is Difficulty.EASY):
            throws = 2

        # The HARD NPC atempts to play smarter
        # and adapt to certain senarios.

        # Here the number of throws the NPC
        # should make is determined.
        elif (self._difficulty_setting is Difficulty.HARD):
            if (npc_score == 0):
                throws = 3
            elif (score_left < 20):
                if (op_lead >= 10):
                    throws = 9
                elif (npc_lead >= 10):
                    throws = 5
                else:
                    throws = 7
            elif (score_left < 30):
                if (op_lead >= 10):
                    throws = 7
                elif (npc_lead >= 10):
                    throws = 4
                else:
                    throws = 6
            elif (score_left < 50):
                if (op_lead >= 10):
                    throws = 5
                elif (npc_lead >= 10):
                    throws = 3
                else:
                    throws = 4
            else:
                if (op_lead >= 20):
                    throws = 6
                elif (npc_lead >= 20):
                    throws = 3
                elif (op_lead >= 10):
                    throws = 5
                elif (npc_lead >= 10):
                    throws = 4
                else:
                    throws = 3

        # This is where the NPCs rolls the dice.
        # The throws value set erlier decides
        # how many times the NPC will roll the dice.

        # The outcome is also checked in the loop to
        # see if a 1 is thrown. If it is then the score
        # this turn is set to 0 and the loop is closed.
        # If the total score equals or exceeds 100 the
        # loop is also closed.
        list_of_outcomes = []
        while (_rolls_this_turn < throws and _run):
            outcome = self._die.roll_dice()
            _rolls_this_turn += 1
            list_of_outcomes.append(outcome)

            if (outcome != 1):
                self._turn_score += outcome
            else:
                self._turn_score = 0
                _run = False

            if (self._total_score + self._turn_score >= 100):
                _run = False

        self._total_score += self.get_turn_score()
        return list_of_outcomes
