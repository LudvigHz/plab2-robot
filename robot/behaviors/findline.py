""" Module for find line sub class """
from ..behavior import Behavior
from ..sensors.irproximity_sensor import IRProximitySensor


class FindLine(Behavior):
    """ Behavior for finding a line when not on one """

    def __init__(self, sensobs, match_threshold=0.2):
        self._sensobs = sensobs
        self._match_threshold = match_threshold
        self.update_sensor_value()

    def consider_deactivation(self):
        # Should deactivate if middle sensors are on the line
        return (
            len(filter(lambda x: x < self._match_threshold, self._raw_values[0][2:4]))
            > 1
        )

    def consider_activation(self):
        # Should activate if no sensors are on the line
        return not filter(lambda x: x < self._match_threshold, self._raw_values[0])

    def update_sensor_value(self):
        """Update raw sensor values"""
        self._raw_values = [sensob.get_values() for sensob in self._sensobs]

    def calculate_match_degree(self):
        """ Return 1 if any sensor on line, otherwise 0 """
        return (
            0 if filter(lambda x: x < self._match_threshold, self._raw_values[0]) else 1
        )

    def sense_and_act(self):
        """ Check sensors and act according to their values """
        self.calculate_match_degree()
        self._weight = self._match_degree * self._priority
        # If 1 of the sensors has a high value
        if filter(lambda x: x < self._match_threshold, self._raw_values[0]):
            self._motor_recommendations = [0.0, 0.0]
        # If no sensors on line, go forward
        else:
            self._motor_recommendations = [0.6, 0.6]
