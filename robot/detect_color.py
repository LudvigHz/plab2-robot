'''File containing the color-detecting class'''

from robot.behavior import Behavior
from robot.sensors.camera import Camera
# imager2.py
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


class DetectColor(Behavior):
    '''Class for detecting color using the Raspicam'''
    _pixel_colors = {
        'red': (
            255, 0, 0), 'green': (
            0, 255, 0), 'blue': (
                0, 0, 255), 'white': (
                    255, 255, 255), 'black': (
                        0, 0, 0)}
    _camera = None
    _value = None
    _color = None  # Color to detect

    def __init__(self, color, bbcon, priority, sensobs):
        '''Color input determines which color the camera should detect: red, green, blue, white or black'''
        super().__init__(bbcon, priority, sensobs)
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = [
            1.0, 0.0]  # recommended to spin, change?
        self._camera = Camera()
        self._color = self._pixel_colors.get(color)

    def reset(self):
        '''Sets the value slot to None'''
        self._camera.reset()
        self._value = None
        self._color = None

    def set_color(self, color):
        '''Set new color to detect'''
        self._color = color

    def take_picture(self):
        '''Takes a picture and updates _value'''
        self._camera.update()
        self._value = self._camera.get_value()  # returns Image-object
        self.analyze_picture()

    def analyze_picture(self):
