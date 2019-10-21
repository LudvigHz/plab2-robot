"""File contains the BBCON class"""


class BBCON:
    """Behavior-Based Controller - checked at each timestep to determine the robot's next move"""

    behaviors = None
    active_behaviors = None
    sensobs = None
    motobs = None
    arbitrator = None

    def add_behavior(self):
        """Append a newly-created behavior onto the behaviors list"""
        return

    def add_sensob(self):
        """Append a newly-created sensob onto the sensobs list"""
        return

    def activate_behavior(self):
        """Add an existing behavior onto the active-behaviors list"""
        return

    def deactivate_behavior(self):
        """Remove an existing behavior from the active behaviors list"""
        return

    def run_one_timestep(self):
        """
        1 - Update Sensobs
        2 - Update Behaviors
        3 - Invoke Arbitrator
        4 - Update Motobs
        5 - Wait
        6 - Reset Sensobs
        """
