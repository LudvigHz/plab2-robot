from robot.arbitrator import Arbitrator
from robot.bbcon import BBCON
from robot.behaviours import FollowLine
from robot.dont_crash_behavior import DontCrashBehavior
from robot.motob import Motob
from robot.sensob import Sensob
from robot.sensors.reflectance_sensors import ReflectanceSensors
from robot.sensors.ultrasonic import Ultrasonic
from robot.sensors.zumo_button import ZumoButton

print("Running test.py")
bbcon = BBCON()
ultra = Sensob([Ultrasonic()])
irarray = Sensob([ReflectanceSensors()])
bbcon.add_sensob(ultra)
bbcon.add_sensob(irarray)
dont_crash = DontCrashBehavior(bbcon, 0.7, [ultra])
follow_line = FollowLine(bbcon, 0.5, [irarray])
bbcon.add_behavior(dont_crash)
bbcon.add_behavior(follow_line)
bbcon.activate_behavior(dont_crash)
bbcon.activate_behavior(follow_line)
ZumoButton().wait_for_press()

while True:
    print("While-loop")
    bbcon.run_one_timestep()
