from robot.arbitrator import Arbitrator
from robot.bbcon import BBCON
from robot.behaviours import FollowLine
from robot.dont_crash_behavior import DontCrashBehavior
from robot.motob import Motob
from robot.move_forward_behavior import MoveForwardBehavior
from robot.sensob import Sensob
from robot.sensors.reflectance_sensors import ReflectanceSensors
from robot.sensors.ultrasonic import Ultrasonic
from robot.sensors.zumo_button import ZumoButton

print("Running test.py")


def test():
    ZumoButton().wait_for_press()

    bbcon = BBCON()

    ultra = Sensob([Ultrasonic()])
    irarray = Sensob([ReflectanceSensors()])

    bbcon.add_sensob(ultra)
    bbcon.add_sensob(irarray)

    dont_crash = DontCrashBehavior(bbcon, 1.0, [ultra])
    follow_line = FollowLine(bbcon, 0.7, [irarray])
    move_forward = MoveForwardBehavior(bbcon, 0.1)

    bbcon.add_behavior(dont_crash)
    bbcon.add_behavior(follow_line)
    bbcon.add_behavior(move_forward)

    i = 0
    while True:
        print("While-loop")
        bbcon.run_one_timestep()
        i += 1
        if i > 50:
            break

    bbcon.stop()
