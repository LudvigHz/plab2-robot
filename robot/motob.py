"""File contains the Motob class"""


class Motob:
    """Interface between Behavior and one or more motor wrappers"""

    _motors = None
    _value = None

    def update(self, motor_recommendations):
        """Receive a list of new motor recommendation, load it into the value slot, and
        operationalize it"""
        return

    def operationalize(self):
        """Convert a motor recommendation into one or more motor settings, which are sent to the
        corresponding motor(s)"""
        return
