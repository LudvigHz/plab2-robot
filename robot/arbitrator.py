"""File contains the Arbitrator class"""
from robot.bbcon import BBCON
from robot.behavior import Behavior
from typing import List


class Arbitrator:
    """Fetches the active Behaviors from BBCON and choses a winner among them"""

    _bbcon: BBCON

    def __init__(self, bbcon: BBCON):
        self._bbcon = bbcon

    def choose_action(self):
        """Fetches the active Behaviors from BBCON and chose the one with highest priority and set
        the action for the BBCON"""

        behaviors: List[Behavior] = self._bbcon.get_active_behaviors()
        priority_behavior = behaviors[0]
        for behavior in behaviors:
            if

    def choose_action_stochastic(self):
        """Fetches the active Bevahiors from BBCON and use weight as probability for them to be
        chosen. Then sets the action for the BBCON"""
        return
