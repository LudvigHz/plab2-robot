"""File contains Dummy_behavior class"""


class DummyBehavior:
    """Dummy class for testing"""

    motor_recommendations = None
    halt_request = None
    weight = None

    def get_weight(self):
        """Getter"""
        return self.weight

    def get_motor_recommendations(self):
        """Getter"""
        return self.motor_recommendations

    def get_halt_request(self):
        """Getter"""
        return self.halt_request

    def update(self):
        """Dummy method"""
        return
