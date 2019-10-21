"""File contains the Arbitrator class"""


class Arbitrator:
    """Fetches the active Behaviors from BBCON and choses a winner among them"""

    bbcon: BBCON

    def __init__(self, bbcon: BBCON):
        self.bbcon = bbcon

    def choose_action(self):
        """Fetches the active Behaciors from BBCON and chose the one with highest priority and set
        the action for the BBCON"""
        return

    def choose_action_stochastic(self):
        """Fetches the active Bevahiors from BBCON and use weight as probability for them to be
        chosen. Then sets the action for the BBCON"""
        return
