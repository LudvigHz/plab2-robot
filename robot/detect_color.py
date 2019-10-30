'''File containing the color-detecting class'''

from robot.behavior import Behavior
from robot.sensors.camera import Camera
from robot.sensors.imager2 import Imager
# from .sensors.motors import Motors


class DetectColor(Behavior):
    '''Class for detecting color using the Raspicam'''
    _color_detected = None
    _camera = None
    _value = None
    _color = None  # Color to detect
    _imager = None  # Imager helper-class
    _timer = None

    def __init__(self, colorname, bbcon, priority, sensobs):
        '''Color input determines which color the camera should detect: red, green, blue, white or black'''
        super().__init__(bbcon, priority, sensobs)
        self._halt_request = False
        self._active_flag = False
        self._motor_recommendations = [0.0, 0.0]  # recommended to stop
        self._halt_request = False
        self._color_detected = False
        self._weight = 0
        self._camera = Camera()
        self._imager = Imager()
        self._color = self._imager.get_color_rgb(colorname)
        self._timer = 0

    def reset(self):
        '''Resets the object'''
        self._camera.reset()
        self._value = None
        self._color = None

    def set_color(self, color):
        '''Set new color to detect'''
        self._color = color

    def take_picture(self, threshold=0.3):
        '''Takes a picture and updates _value, threshold is the percentage of the pixels which should match _color'''
        self._camera.update()
        self._value = self._camera.get_value()  # returns Image-object
        self._color_detected = self.analyze_picture(threshold)

    def analyze_picture(self, threshold):
        '''Returns a boolean, determining if the picture is a match with _color'''
        mapped_image = self._imager.map_color_wta()
        # iterate through the entire image matrix and check pixel color against
        # local _color variable
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

    def consider_deactivation(self):
        '''Deactivate if active, take pictures in intervals'''
        self._active_flag = False

    def consider_activation(self):
        '''Activate if _timer is high enough (take pictures in intervals of 10*timestep (10*0.5s))'''
        if self._timer > 10:
            self._active_flag = True
            self._timer = 0
        else:
            self._timer += 1

    def _sense_and_act(self):
        '''Calculate weight'''
        self.take_picture()
        self._weight = self._priority * self._match_degree

    def update(self):
        """The main interface between the bbcon and the behavior:
        1 - Update the activity status
        2 - Call sense and act
        3 - Update the behavior’s weight
        """
        if self._active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        self._sense_and_act()