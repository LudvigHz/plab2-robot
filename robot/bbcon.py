"""File contains the BBCON class"""

from robot.arbitrator import Arbitrator


class BBCON:
    """Behavior-Based Controller - checked at each timestep to determine the robot's next move"""

    "Config"
    _stochastic = False

    _behaviors = []
    _active_behaviors = []
    _sensobs = []
    _motobs = []
    _arbitrator = None

    def __init__(self):
        self._arbitrator = Arbitrator(self)

    def add_behavior(self, behavior):
        """Append a newly-created behavior onto the behaviors list"""
        self._behaviors.append(behavior)

    def add_sensob(self, sensob):
        """Append a newly-created sensob onto the sensobs list"""
        self._sensobs.append(sensob)

    def activate_behavior(self, behavior):
        """Add an existing behavior onto the active-behaviors list"""
        self._active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        """Remove an existing behavior from the active behaviors list"""
        self._active_behaviors.remove(behavior)

    def run_one_timestep(self):
        """
        1 - Update Sensobs
        2 - Update Behaviors
        3 - Invoke Arbitrator
        4 - Update Motobs
        5 - Wait
        6 - Reset Sensobs
        """

        for sensor in self._sensobs:
            sensor.update()

        for behavior in self._behaviors:
            behavior.update()

        if self._stochastic:
            motor_recommendations, halt_request = self._arbitrator.choose_action_stochastic()
        else:
            motor_recommendations, halt_request = self._arbitrator.choose_action()

        if halt_request:
            # TODO halt run
            return

        for motob in self._motobs:
            motob.update(motor_recommendations)


    def get_active_behaviors(self):
        """Getter"""
        return self._active_behaviors
