from robot.arbitrator import Arbitrator
from robot.bbcon import BBCON
from robot.behaviours import FollowLine
from robot.dont_crash_behavior import DontCrashBehavior
from robot.motob import Motob
from robot.sensob import Sensob
from robot.sensors.reflectance_sensors import ReflectanceSensors
from robot.sensors.ultrasonic import Ultrasonic

bbcon = BBCON()
ultra = Sensob([Ultrasonic()])
irarray = Sensob([ReflectanceSensors()])
bbcon.add_sensob(ultra)
bbcon.add_sensob(irarray)
bbcon.add_behavior(DontCrashBehavior(bbcon, 0.7, [ultra]))
bbcon.add_behavior(FollowLine(bbcon, 0.5, [irarray]))


while True:
    bbcon.run_one_timestep()
