"""File contains the Motob class"""
from .sensors.motors import Motors


class Motob:
    """Interface between Behavior and one or more motor wrappers"""

    _motors = None
    _value = None

    def __init__(self):
        self._motors = Motors()

    def update(self, motor_recommendations):
        """Receive a list of new motor recommendation, load it into the value slot, and
        operationalize it"""
        self._value = motor_recommendations
        self.operationalize()

    def operationalize(self):
        """Convert a motor recommendation into one or more motor settings, which are sent to the
        corresponding motor(s)"""
        self._motors.set_value(self._value)
