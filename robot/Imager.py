from PIL import Image


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
        self.init_file_info(fname, dir, ext)
        self.image = image  # A PIL image object
        self.xmax = width
        self.ymax = height  # These can change if there’s an input image or file
        self.mode = mode
        self.init_image(background=background)

    def init_file_info(self, fname=None, dir=None, ext=None):
        self.dir = dir if dir else self._image_dir_
        self.ext = ext if ext else self._image_ext_
        self.fid = self.gen_fid(fname) if fname else None

    def gen_fid(self, fname, dir=None, ext=None):
        dir = dir if dir else self.dir
        ext = ext if ext else self.ext
        return dir + fname + "." + ext

    def init_image(self, background='black'):
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
        fname = fid.split('.')
        type = fname[1] if len(fname) > 1 else type
        self.image.save(fname[0] + '.' + type, format=type)

    def get_image(self): return self.image

    def set_image(self, im): self.image = im

    def display(self): self.image.show()

    def get_image_dims(self):
        self.xmax = self.image.size[0]
        self.ymax = self.image.size[1]

    def gen_plain_image(self, w, h, color, mode='RGB'):
        return Image.new(mode, (w, h), self.get_color_rgb(color))

    def get_color_rgb(self, colorname): return Imager._pixel_colors[colorname]

    def resize(self, new_width, new_height):
        return Imager(image=self.image.resize((new_width, new_height)))

    def scale(self, xfactor, yfactor):
        return self.resize(
            round(
                xfactor *
                self.xmax),
            round(
                yfactor *
                self.ymax))
