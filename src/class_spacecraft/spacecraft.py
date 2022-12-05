

import utils.setup as sp


class Spacecraft:

    def __init__(self, x, y, z, imag):
        self.x = x
        self.y = y
        self.z = z
        self.h = sp.SPCRFT_H0*z
        self.w = sp.SPCRFT_W0*z
        self.img = imag

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))














