import utils.setup as sp
from pygame.transform import scale

class Spacecraft:
    def __init__(self, x, y, imag):
        self.f = sp.SPCRAFT_F2
        self.w = sp.SPCRAFT_W0 * self.f
        self.h = sp.SPCRAFT_H0 * self.f
        self.x = (1-x)*sp.WIN_WIDTH - self.w/2
        self.y = y*sp.WIN_HEIGHT - self.h/2
        self.z = 1
        self.imag = imag 

    def draw(self, win):
        win.blit(self.imag, [self.x, self.y])

    def update(self, x, y, z, imag):
        self.z = z
        self.f = abs((-(sp.SPCRAFT_F1-1)*z/0.7 + 1)*sp.SPCRAFT_F2)
        self.w = sp.SPCRAFT_W0 * self.f
        self.h = sp.SPCRAFT_H0 * self.f
        self.x = (1-x)*sp.WIN_WIDTH-self.w/2
        self.y = y*sp.WIN_HEIGHT-self.h/2
        self.imag = scale(imag, (self.w, self.h))
       
        self.limits()

    def limits(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= sp.WIN_WIDTH-self.w:
            self.x = sp.WIN_WIDTH-self.w

        if self.y <= 0:
            self.y = 0
        elif self.y >= sp.WIN_HEIGHT-self.h:
            self.y = sp.WIN_HEIGHT-self.h
