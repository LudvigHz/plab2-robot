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

    def __init__(
        self, bbcon, priority, sensobs, colorname="red", motor_recommendation=[-1, -1]
    ):
        """Color input determines which color the camera should detect: red, green, blue, white or black,
        default is red"""
        super().__init__(bbcon, priority, sensobs)
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = motor_recommendation  # recommended to stop
        self._halt_request = False
        self._color_detected = False
        self._weight = 0
        self._imager = Imager(height=32, width=32)
        self._color = colorname
        self._timer = 0

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

        mapped_image.get_image_dims()
        width = mapped_image.xmax
        height = mapped_image.ymax
        red = 0
        green = 0
        blue = 0
        for pixel in range(width):
            for pixel2 in range(height):
                pixel_color = mapped_image.get_pixel(pixel, pixel2)
                if pixel_color[0] > 150:
                    red += 1
                elif pixel_color[1] > 150:
                    green += 1
                elif pixel_color[2] > 150:
                    blue += 1
        self._red_match_degree = red / (width * height)
        self._green_match_degree = green / (width * height)
        self._blue_match_degree = blue / (width * height)
        if self._color == "red":
            self._match_degree = self._red_match_degree
            return self._red_match_degree > threshold
        if self._color == "green":
            self._match_degree = self._green_match_degree
            return self._green_match_degree > threshold
        if self._color == "blue":
            self._match_degree = self._blue_match_degree
            return self._blue_match_degree > threshold
        else:
            return False

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
        self._imager.set_image(self._value)
        self._color_detected = self.analyze_picture(0.75)
        self._weight = self._priority * self._match_degree
        print("\n\n\t\t\tIMAGER STUFF")
        print("\t\tDETECTED", self._color_detected)
        print("\t\tMATCH DEGREE", self._match_degree)
        print("\t\tWEIGHT", self._weight)
