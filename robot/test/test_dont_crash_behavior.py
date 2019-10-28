"""File contains tests for DontCrashBehavior class"""

import unittest

from robot.dont_crash_behavior import DontCrashBehavior
from robot.test.dummysensob import DummySensob


class MyTestCase(unittest.TestCase):
    """Test DontCrashBehavior class"""

    def setUp(self) -> None:
        """Sets up"""
        self.dont_crash_behavior = DontCrashBehavior(None, None, None)
        self.sensob = DummySensob()

    def test_consider_activation(self):
        """Test consider_activation()"""
        self.sensob.values = [20]
        self.dont_crash_behavior._sensobs = [self.sensob]
        self.assertFalse(self.dont_crash_behavior._active_flag)
        self.dont_crash_behavior.consider_activation()
        self.assertTrue(self.dont_crash_behavior._active_flag)

    def test_consider_deactivation(self):
        """Test consider_deactivation"""
        self.dont_crash_behavior._active_flag = True
        self.assertTrue(self.dont_crash_behavior._active_flag)
        self.sensob.values = [40]
        self.dont_crash_behavior._sensobs = [self.sensob]
        self.dont_crash_behavior.consider_deactivation()
        self.assertFalse(self.dont_crash_behavior._active_flag)

    def test_sense_and_act(self):
        """Test sense_and_act"""
        self._raw_values = [20]


if __name__ == '__main__':
    unittest.main()
