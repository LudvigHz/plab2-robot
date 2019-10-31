"""File containing the color-detecting class"""

from robot.behavior import Behavior
from robot.sensors.camera import Camera
from robot.sensors.imager2 import Imager

# from .sensors.motors import Motors


class DetectColor(Behavior):
    """Class for detecting color using the Raspicam"""

    _color_detected = None
    _camera = None
    _value = None
    _color = None  # Color to detect
    _imager = None  # Imager helper-class
    _timer = None

    def __init__(self, bbcon, sensobs, priority, colorname="red"):
        """Color input determines which color the camera should detect: red, green, blue, white or black,
        default is red"""
        super().__init__(bbcon, priority, sensobs)
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = [-1.0, -1.0]  # recommended to stop
        self._halt_request = False
        self._color_detected = False
        self._weight = 0
        self._color = self._imager.get_color_rgb(colorname)
        self._timer = 0
        self._imager = Imager()

    def reset(self):
        """Resets the object"""
        self._value = None
        self._color = None

    def set_color(self, color):
        """Set new color to detect"""
        self._color = color

    def analyze_picture(self, threshold):
        """Returns a boolean, determining if the picture is a match with _color"""
        mapped_image = self._imager.map_color_wta()
        # iterate through the entire image matrix and check pixel color against
        # local _color variable
        self._imager.set_image(mapped_image)
        width = self._imager.xmax
        height = self._imager.ymax
        counter = 0
        for pixel in range(height):
            for pixel2 in range(width):
                pixel_color = self._imager.get_pixel(pixel, pixel2)
                if pixel_color == self._color:
                    counter += 1
        self._match_degree = counter / (width * height)
        return self._match_degree > threshold

    def _consider_deactivation(self):
        """Deactivate if no obstacle is detected"""
        if not (self._bbcon.get_obstacle_detected_flag()):
            self._active_flag = False

    def _consider_activation(self):
        """Activate if obstacle is detected"""
        if self._bbcon.get_obstacle_detected_flag():
            self._active_flag = True

    def _sense_and_act(self):
        """Calculate weight"""
        self._value = self._raw_values[0][0]
        self._color_detected = self.analyze_picture(0.25)
        self._weight = self._priority * self._match_degree
