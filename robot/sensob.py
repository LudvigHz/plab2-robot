"""File contains the Sensob class"""


class Sensob:
    """Interface between Behavior and the sensor wrappers"""

    def update(self):
        """Fetch the relevant sensor value(s) and convert them into the pre-processed sensob
        value"""
        return

    def reset(self):
        """Reset the sensor(s) if applicable"""
        return
