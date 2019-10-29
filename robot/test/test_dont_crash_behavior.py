"""File contains tests for DontCrashBehavior class"""

import unittest

from robot.dont_crash_behavior import DontCrashBehavior


class MyTestCase(unittest.TestCase):
    """Test DontCrashBehavior class"""

    def setUp(self) -> None:
        """Sets up"""
        self.dont_crash_behavior = DontCrashBehavior(None, None, None)

    def test_consider_activation(self):
        """Test consider_activation()"""
        self.dont_crash_behavior._raw_values = [20]
        self.assertFalse(self.dont_crash_behavior._active_flag)
        self.dont_crash_behavior.consider_activation()
        self.assertTrue(self.dont_crash_behavior._active_flag)

    def test_consider_deactivation(self):
        """Test consider_deactivation"""
        self.dont_crash_behavior._active_flag = True
        self.assertTrue(self.dont_crash_behavior._active_flag)
        self.dont_crash_behavior._raw_values = [40]
        self.dont_crash_behavior.consider_deactivation()
        self.assertFalse(self.dont_crash_behavior._active_flag)

    def test_sense_and_act(self):
        """Test sense_and_act"""
        self.dont_crash_behavior._threshold_distance = 30
        self.dont_crash_behavior._stop_distance = 10
        self.dont_crash_behavior._raw_values = [5]
        self.dont_crash_behavior._priority = 0.5
        self.dont_crash_behavior._sense_and_act()
        self.assertEqual(self.dont_crash_behavior._match_degree, 1)

        self.dont_crash_behavior._raw_values = [20]
        self.dont_crash_behavior._sense_and_act()
        self.assertEqual(self.dont_crash_behavior._match_degree, 0.5)

        self.dont_crash_behavior._raw_values = [30]
        self.dont_crash_behavior._sense_and_act()
        self.assertEqual(self.dont_crash_behavior._match_degree, 0)


if __name__ == "__main__":
    unittest.main()
