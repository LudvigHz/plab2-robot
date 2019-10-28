"""File contains the Sensob class"""


class Sensob:
    """Interface between Behavior and the sensor wrappers"""

    _wrappers = []
    _values = []

    def __init__(self, wrappers):
        self._wrappers = wrappers
        for wrapper in wrappers:
            wrapper.__init__()

    def update(self):
        """Fetch the relevant sensor value(s) and convert them into the pre-processed sensob
        value"""
        for wrapper in self._wrappers:
            wrapper.update()

        for i in range(len(self._wrappers)):
            value = self._wrappers[i].get_value()
            self._values[i] = value

    def get_values(self):
        """ Returns the sensor values """
        return self._values

    def reset(self):
        """Reset the sensor(s) if applicable"""
        for wrapper in self._wrappers:
            wrapper.reset()
