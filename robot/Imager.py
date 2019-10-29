'''File containing the Imager class'''

from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance


class Imager():
    '''Helper-class to handle images'''
    _pixel_colors = {
        'red': (
            255, 0, 0), 'green': (
            0, 255, 0), 'blue': (
                0, 0, 255), 'white': (
                    255, 255, 255), 'black': (
                        0, 0, 0)}
    _image_dir_ = "images/"
    _image_ext_ = "jpeg"

    def __init__(
            self,
            fname=False,
            dir=None,
            ext=None,
            image=None,
            width=100,
            height=100,
            background='black',
            mode='RGB'):
        '''Initializes the class'''
        self.init_file_info(fname, dir, ext)
        self.image = image  # A PIL image object
        self.xmax = width
        self.ymax = height  # These can change if there’s an input image or file
        self.mode = mode
        self.init_image(background=background)

    def init_file_info(self, fname=None, dir=None, ext=None):
        '''Info on picture file'''
        self.dir = dir if dir else self._image_dir_
        self.ext = ext if ext else self._image_ext_
        self.fid = self.gen_fid(fname) if fname else None

    def gen_fid(self, fname, dir=None, ext=None):
        '''Generates file ID'''
        dir = dir if dir else self.dir
        ext = ext if ext else self.ext
        return dir + fname + "." + ext

    def init_image(self, background='black'):
        '''Initializes image'''
        if self.fid:
            self.load_image()
        if self.image:
            self.get_image_dims()
        else:
            self.image = self.gen_plain_image(self.xmax, self.ymax, background)

    def load_image(self):
        '''Load image from file'''
        self.image = Image.open(
            self.fid)  # the image is actually loaded as needed (automatically by PIL)
        if self.image.mode != self.mode:
            self.image = self.image.convert(self.mode)
        # Save image to a file. Only if fid has no extension is the type
        # argument used.

    def dump_image(self, fid, type='gif'):
        '''Save image'''
        fname = fid.split('.')
        type = fname[1] if len(fname) > 1 else type
        self.image.save(fname[0] + '.' + type, format=type)

    def get_image(self):
        '''Returns image'''
        return self.image

    def set_image(self, im):
        '''Sets image'''
        self.image = im

    def display(self):
        '''Displays image'''
        self.image.show()

    def get_image_dims(self):
        '''Get the image dimensions'''
        self.xmax = self.image.size[0]
        self.ymax = self.image.size[1]

    def gen_plain_image(self, w, h, color, mode='RGB'):
        '''Generate a plain image'''
        return Image.new(mode, (w, h), self.get_color_rgb(color))

    def get_color_rgb(self, colorname):
        '''Converts color'''
        return Imager._pixel_colors[colorname]

    def resize(self, new_width, new_height):
        '''Resize image'''
        return Imager(image=self.image.resize((new_width, new_height)))

    def scale(self, xfactor, yfactor):
        '''Scale image'''
        return self.resize(
            round(
                xfactor *
                self.xmax),
            round(
                yfactor *
                self.ymax))

    def get_pixel(self, x, y):
        '''Get pixel'''
        return self.image.getpixel((x, y))

    def set_pixel(self, x, y, rgb):
        '''Set pixel'''
        self.image.putpixel((x, y), rgb)

    def combine_pixels(self, p1, p2, alpha=0.5):
        '''Combines pixels with factor alpha'''
        return tuple([round(alpha * p1[i] + (1 - alpha) * p2[i])
                      for i in range(3)])

    def map_image(self, func):
        '''Map image'''
        return Imager(
            image=Image.eval(
                self.image,
                func))  # eval creates a new image.

    def map_image2(self, func):
        '''Image mapper helper function'''
        im2 = self.image.copy()
        for i in range(self.xmax):
            for j in range(self.ymax):
                im2.putpixel((i, j), func(im2.getpixel((i, j))))
        return Imager(image=im2)

    def map_color_wta(self, thresh=0.34):
        '''"Winner takes all"-map of image'''
        def wta(p):  # p is an RGB tuple
            '''Local function'''
            s = sum(p)
            w = max(p)
            if s > 0 and w / s >= thresh:
                return tuple([(x if x == w else 0) for x in p])
            else:
                return (0, 0, 0)
        return self.map_image2(wta, self.image)
