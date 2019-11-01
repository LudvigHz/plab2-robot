"""File contains the AvoidTapeBehavior"""
from robot.behavior import Behavior


class AvoidTapeBehavior(Behavior):
    """Behavior that backs up and rotates when encountering tape"""

    # Config
    _threshold = 0.2

    _remain_active = False

    def _consider_deactivation(self):
        """Checks if it has to perform turn"""
        if self._remain_active:
            self._motor_recommendations = [-0.5, 0.5]
        else:
            self._active_flag = False
        self._remain_active = False

    def _consider_activation(self):
        """Check if tape is detected"""
        for sensor_value in self._raw_values[0][0]:
            if sensor_value < self._threshold:
                self._active_flag = True
                self._remain_active = True
                self._motor_recommendations = [-0.5, -0.5]

    def _sense_and_act(self):
        self._weight = self._priority
