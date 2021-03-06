"""File contains the DontCrashBehavior class"""

from robot.behavior import Behavior


class DontCrashBehavior(Behavior):
    """Behavior that uses the UltraSonic Sensob to not crash"""

    # Config
    _threshold_distance = 8
    _stop_distance = 5

    def __init__(self, bbcon, priority, sensobs):
        super().__init__(bbcon, priority, sensobs)
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = [0.0, 0.0]

    def _consider_deactivation(self):
        """If no obstacle is detected, then deactivate"""
        for value in self._raw_values[0]:
            if value < self._threshold_distance and value != 0:
                return
        self._active_flag = False
        self._bbcon.set_obstacle_detected_flag(False)

    def _consider_activation(self):
        """If an obstacle is detected, then activate"""
        for value in self._raw_values[0]:
            if value < self._threshold_distance and value != 0:
                self._active_flag = True
                self._bbcon.set_obstacle_detected_flag(True)
                return

    def _sense_and_act(self):
        """Calculate weight, don't generate halt requests. Average _raw_values in case there are
        several. _raw_values must be in cm"""
        print("\t\tDONT CRASH VAL:", self._raw_values)
        distance = sum(self._raw_values[0]) / len(self._raw_values)
        degree = 1
        if distance > self._stop_distance:
            degree = (self._threshold_distance - distance) / (
                self._threshold_distance - self._stop_distance
            )
        self._match_degree = degree
        self._weight = self._match_degree * self._priority
