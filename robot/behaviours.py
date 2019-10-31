from .behavior import Behavior
from .sensob import Sensob
from .sensors.irproximity_sensor import IRProximitySensor


class FollowLine(Behavior):

    _halt_request = False

    def _consider_deactivation(self):
        self.calculate_match_degree()
        if self._match_degree < 3:
            self._active_flag = False

    def _consider_activation(self):
        self.calculate_match_degree()
        if self._match_degree >= 3:
            self._active_flag = True

    def calculate_match_degree(self):
        """Calculate match. Darker reading on the edges give higher values"""
        sum(
            [i * (1 - val) for i, val in enumerate(self._raw_values[0][0][2::-1])]
        ) + sum([i * (1 - val) for i, val in enumerate(self._raw_values[0][0][3:])])

    def _sense_and_act(self):
        self.calculate_match_degree()
        self._weight = self._match_degree * self._priority
        # If 1 of the leftmost sensors hava a value higher than 0.2, turn left
        if len(list(filter(lambda x: x < 0.6, self._raw_values[0][0][:2]))) > 1:
            self._motor_recommendations = [0.1, 0.8]
        # If 1 of the rightmost sensors hava a value higher than 0.2, turn right
        elif len(list(filter(lambda x: x < 0.6, self._raw_values[0][0][4:]))) > 1:
            self._motor_recommendations = [0.8, 0.1]
        else:
            self._motor_recommendations = [0.4, 0.4]
