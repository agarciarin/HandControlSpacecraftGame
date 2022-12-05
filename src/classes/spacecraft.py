import utils.setup as sp

class Spacecraft:
    def __init__(self, x, y, imag):
        self.x = x
        self.y = y
        self.z = 1
        self.h = sp.SPCRAFT_H0
        self.w = sp.SPCRAFT_W0
        self.img = imag

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z