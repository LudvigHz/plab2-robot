"""File contains the DontCrashBehavior class"""

from robot.behavior import Behavior


class DontCrashBehavior(Behavior):
    """Behavior that uses the UltraSonic Sensob to not crash"""

    # Config
    _threshold_distance = 30
    _stop_distance = 10

    def __init__(self):
        super().__init__()
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = [0.0, 0.0]

    def consider_deactivation(self):
        """If no obstacle is detected, then deactivate"""
        for sensob in self._sensobs:
            for value in sensob.get_values():
                if value < self._threshold_distance:
                    return
        self._active_flag = False

    def consider_activation(self):
        """If an obstacle is detected, then activate"""
        for sensob in self._sensobs:
            for value in sensob.get_values():
                if value < self._threshold_distance:
                    self._active_flag = True
                    return

    def sense_and_act(self):
        """Calculate weight, don't generate halt requests"""
        self._weight = (
            (sum(self._raw_values) / len(self._raw_values)) - self._stop_distance
        ) * self._priority
