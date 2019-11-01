"""File contains the Sensob class"""
from time import perf_counter


class Sensob:
    """Interface between Behavior and the sensor wrappers"""

    _wrappers = []
    _values = []
    _delay = 1.0
    _last_time = 0.0

    def __init__(self, wrappers, delay=0.0):
        self._wrappers = wrappers
        self._values = [None] * len(wrappers)
        self._delay = delay

    def update(self):
        """Fetch the relevant sensor value(s) and convert them into the pre-processed sensob
        value"""
        if (perf_counter() - self._last_time) > self._delay:
            for wrapper in self._wrappers:
                wrapper.update()

            for i in range(len(self._wrappers)):
                value = self._wrappers[i].get_value()
                self._values[i] = value

            self._last_time = perf_counter()

    def get_values(self):
        """ Returns the sensor values """
        return self._values

    def reset(self):
        """Reset the sensor(s) if applicable"""

        if (perf_counter() - self._last_time) > self._delay:
            for wrapper in self._wrappers:
                wrapper.reset()
