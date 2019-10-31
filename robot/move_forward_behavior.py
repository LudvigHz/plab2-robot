"""File contains the MoveForwardBehavior class"""

from robot.behavior import Behavior


class MoveForwardBehavior(Behavior):
    """A Behavior that moves forward without using sensors"""

    def __init__(self, bbcon, priority=1, sensobs=[]):
        super().__init__(bbcon, priority, sensobs)
        self._motor_recommendations = [0.5, 0.5]
        self._active_flag = True
        self._halt_request = False
        self._weight = 1 * priority

    def _consider_deactivation(self):
        """Doesn't consider deactivation"""
        pass

    def _consider_activation(self):
        """Doesn't consider activation"""
        pass

    def _sense_and_act(self):
        """Doesn't sense or act"""
        pass
