"""File contains tests for BBCON class"""

import unittest

from robot.bbcon import BBCON
from robot.test.dummybehavior import DummyBehavior


class MyTestCase(unittest.TestCase):
    """Tests"""

    def setUp(self) -> None:
        """Set up before tests"""
        self.bbcon = BBCON()
        self.behavior1 = DummyBehavior()

    def test_activate_deactivate_behavior(self):
        """Test activate_behavior"""

        self.assertEqual(0, len(self.bbcon.get_active_behaviors()))

        self.bbcon.activate_behavior(self.behavior1)
        self.assertEqual(1, len(self.bbcon.get_active_behaviors()))

        self.bbcon.deactivate_behavior(self.behavior1)
        self.assertEqual(0, len(self.bbcon.get_active_behaviors()))

    def test_run_one_timestep(self):
        """Test run_one_timestep()"""

        self.bbcon.add_behavior(self.behavior1)
        self.bbcon.activate_behavior(self.behavior1)
        self.bbcon.run_one_timestep()


if __name__ == "__main__":
    unittest.main()
