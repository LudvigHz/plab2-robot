"""File contains Behavior class"""
from abc import abstractmethod


class Behavior:
    """Modular unit designed to analyze a subset of the sensory information as the basis for
    determining a motor request"""

    _bbcon = None
    _sensobs = []
    _motor_recommendations = None
    _active_flag = None
    _halt_request = None
    _priority = None
    _match_degree = None
    _weight = None
    _raw_values = None

    def __init__(self, bbcon, priority, sensobs):
        self._bbcon = bbcon
        self._priority = priority
        self._sensobs = sensobs

    @abstractmethod
    def _consider_deactivation(self):
        """Whenever a behavior is active, it should test whether it should deactivate"""
        raise NotImplementedError

    @abstractmethod
    def _consider_activation(self):
        """Whenever a behavior is inactive, it should test whether it should activate"""
        raise NotImplementedError

    def update_sensor_value(self):
        """Update raw sensor values"""
        self._raw_values = [sensob.get_values() for sensob in self._sensobs]

    def update(self):
        """The main interface between the bbcon and the behavior:
        1 - Update the activity status
        2 - Call sense and act
        3 - Update the behavior’s weight
        """

        self.update_sensor_value()
        if self._active_flag:
            self._consider_deactivation
        else:
            self._consider_activation

        self._sense_and_act()

    @abstractmethod
    def _sense_and_act(self):
        """the core computations performed by the behavior that use sensob readings to produce
        motor recommendations (and halt requests)"""
        raise NotImplementedError

    def get_weight(self):
        """Getter"""
        return self._weight

    def get_motor_recommendations(self):
        """Getter"""
        return self._motor_recommendations

    def get_halt_request(self):
        """Getter"""
        return self._halt_request
