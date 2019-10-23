"""File contains the Arbitrator class"""
from robot.bbcon import BBCON
from robot.behavior import Behavior
from typing import List


class Arbitrator:
    """Fetches the active Behaviors from BBCON and choses a winner among them"""

    _bbcon: BBCON

    def __init__(self, bbcon):
        self._bbcon = bbcon

    def choose_action(self):
        """Fetches the active Behaviors from BBCON and chose the one with highest priority and
        returns a tuple with the motor recommendation and flag for if the run should be halted. If
        several Behaviors have the same priority, the first is chosen"""

        behaviors = self._bbcon.get_active_behaviors()
        priority_behavior = behaviors[0]
        for i in range(1, len(behaviors)):
            if priority_behavior.get_priority() < behaviors[i].get_priority():
                priority_behavior = behaviors[i]
        return priority_behavior.get_motor_recommendations(), priority_behavior.get_halt_request()

    def choose_action_stochastic(self):
        """Fetches the active Bevahiors from BBCON and use weight as probability for them to be
        chosen. Then returns a tuple with the motor recommendation and flag for if the run should
        be halted"""
        return
