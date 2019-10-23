"""Tests for Arbitrator"""

import unittest

from robot.arbitrator import Arbitrator
from robot.test.dummybbcon import DummyBBCON
from robot.test.dummybehavior import DummyBehavior


class MyTestCase(unittest.TestCase):
    """Test class"""

    def setUp(self) -> None:
        """Sets up for testing"""

        self.motor_recommendations1 = ["ONE", "TWO"]
        self.motor_recommendations2 = ["THREE", "FOUR"]

        self.behavior1 = DummyBehavior()
        self.behavior1.halt_request = False
        self.behavior1.priority = 0.6
        self.behavior1.motor_recommendations = self.motor_recommendations1

        self.behavior2 = DummyBehavior()
        self.behavior2.halt_request = True
        self.behavior2.priority = 0.8
        self.behavior2.motor_recommendations = self.motor_recommendations2

        self.bbcon = DummyBBCON()
        self.bbcon.active_behaviors = [self.behavior1, self.behavior2]

        self.arbitrator = Arbitrator(self.bbcon)

    def test_choose_action(self) -> None:
        """Tests .choose_action"""

        self.assertEqual(
            (self.motor_recommendations2, True), self.arbitrator.choose_action()
        )


if __name__ == "__main__":
    unittest.main()
