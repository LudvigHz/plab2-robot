from .behavior import Behavior
from .sensob import Sensob
from .sensors.irproximity_sensor import IRProximitySensor


class FollowLine(Behavior):

    _sensobs = [Sensob([IRProximitySensor])]
    _halt_request = False

    def consider_deactivation(self):
        self.calculate_match_degree()
        if self._match_degree < 2:
            self._active_flag = False

    def consider_activation(self):
        self.calculate_match_degree()
        if self._match_degree >= 2:
            self._active_flag = True

    def update_sensor_value(self):
        """Update raw sensor values"""
        self._raw_values = [sensob.get_values() for sensob in self._sensobs]

    def calculate_match_degree(self):
        """Calculate match. Darker reading on the edges give higher values"""
        self._match_degree = sum(
            [i * (1 - val) for i, val in enumerate(self._raw_values[0][2::-1])]
        )
        self._match_degree += sum(
            [i * (1 - val) for i, val in enumerate(self._raw_values[0][3:])]
        )

    def sense_and_act(self):
        self.calculate_match_degree()
        self._weight = self._match_degree * self._priority
        # If 1 of the leftmost sensors hava a value higher than 0.2, turn left
        if len(filter(lambda x: x < 0.3, self._raw_values[0][:2])) > 1:
            self._motor_recommendations = [0.2, 0.8]
        # If 1 of the rightmost sensors hava a value higher than 0.2, turn right
        elif len(filter(lambda x: x < 0.3, self._raw_values[0][3:])) > 1:
            self._motor_recommendations = [0.8, 0.2]
        else:
            self._motor_recommendations = [0.6, 0.6]
