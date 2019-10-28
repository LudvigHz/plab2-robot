"""File contains Behavior class"""


class Behavior:
    """Modular unit designed to analyze a subset of the sensory information as the basis for
    determining a motor request"""

    _bbcon = None
    _sensobs = None
    _motor_recommendations = None
    _active_flag = None
    _halt_request = None
    _priority = None
    _match_degree = None
    _weight = None

    def consider_deactivation(self):
        """Whenever a behavior is active, it should test whether it should deactivate"""
        return

    def consider_activation(self):
        """Whenever a behavior is inactive, it should test whether it should activate"""
        return

    def update(self):
        """The main interface between the bbcon and the behavior:
        1 - Update the activity status
        2 - Call sense and act
        3 - Update the behavior’s weight
        """
        return

    def sense_and_act(self):
        """the core computations performed by the behavior that use sensob readings to produce
        motor recommendations (and halt requests)"""
        return

    def get_weight(self):
        """Getter"""
        return self._weight

    def get_motor_recommendations(self):
        """Getter"""
        return self._motor_recommendations

    def get_halt_request(self):
        """Getter"""
        return self._halt_request
