"""File contains the DontCrashBehavior class"""

from robot.behavior import Behavior


class DontCrashBehavior(Behavior):
    """Behavior that uses the UltraSonic Sensob to not crash"""

    # Config
    _threshold_distance = 20

    def __init__(self):
        super().__init__()
        self._halt_request = False
        self._active_flag = False

    def consider_deactivation(self):
        """If no obstacle is detected, then deactivate"""
        return

    def consider_activation(self):
        """If an obstacle is detected, then activate"""
        return

    def sense_and_act(self):
        """Calculate weight, generate motor recommendations, don't generate halt requests"""
        return
