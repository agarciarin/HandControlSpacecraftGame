import utils.setup as sp

class Spacecraft:
    def __init__(self, x, y, imag):
        self.x = (1-x)*sp.WIN_WIDTH-sp.SPCRAFT_W0/2
        self.y = y*sp.WIN_HEIGHT-sp.SPCRAFT_H0/2
        self.z = 1
        self.h = sp.SPCRAFT_H0
        self.w = sp.SPCRAFT_W0
        self.img = imag

    def draw(self, win):
        win.blit(self.img, [self.x, self.y])

    def update(self, x, y, z):
        self.x = (1-x)*sp.WIN_WIDTH-self.w/2
        self.y = y*sp.WIN_HEIGHT-self.h/2
        self.z = z
