import utils.setup as sp
from random import uniform, randint
from pygame.transform import rotate, rotozoom
from math import cos, sin, radians
from numpy import array

class Asteroid:
    def __init__(self, imag, rotation): #(image, True/False)
        self.f = uniform(sp.ASTER_F1, 1)
        self.w = sp.ASTER_W0_H0*self.f
        self.h = sp.ASTER_W0_H0*self.f
        #self.x = sp.WIN_WIDTH*(1+sp.ASTER_X0) - self.w/2
        self.x = 1600
        #self.y = uniform( sp.WIN_HEIGHT*(1-sp.ASTER_Y0)/2, sp.WIN_HEIGHT*((1+sp.ASTER_Y0)/2) ) - self.h/2
        self.y = 500
        #self.vel = uniform(sp.ASTER_VEL_MIN, sp.ASTER_VEL_MAX)
        self.vel = 200
        #self.alpha = uniform(-sp.ASTER_ALPHA, sp.ASTER_ALPHA)
        self.alpha = 10
        self.rot = rotation
        #self.vrot = uniform(-sp.ASTER_VROT_RANGE, sp.ASTER_VROT_RANGE)
        self.vrot = 50
        self.beta = 0
        self.imag0 = rotozoom(imag, -self.alpha, self.f)
        self.imag = self.imag0
        self.life = True

    def draw(self, win):
        win.blit(self.imag, self.get_pos())

    def get_pos(self): #return [x, y] image's center
        return array([self.x-self.w/2, self.y-self.h/2])
    
    def get_x(self):
        return self.x-self.w/2

    def get_y(self):
        return self.y-self.h/2

    def update(self, dt):
        if self.rot:
            self.imag = rotate(self.imag0, self.vrot*dt + self.beta)
            self.beta = self.vrot*dt + self.beta

        self.w = self.imag.get_width()
        self.h = self.imag.get_height()
        self.x = self.x - self.vel*dt*cos(radians(self.alpha))
        self.y = self.y - self.vel*dt*sin(radians(self.alpha))
        self.life = self.end_life()
     
    def end_life(self):
        a = self.get_x() <= -sp.END_ASTER_LIFE
        b = self.get_y() <= -sp.END_ASTER_LIFE
        c = self.get_y() >= sp.WIN_HEIGHT + sp.END_ASTER_LIFE

        return a or b or c


class ListAsteroids:
    def __init__(self):
        self.list = []
        self.n = 0
        self.t = 0
        self.aux = 0

    def update(self, t, aster_imags):
        if self.t > 5:
            self.aux = t
            self.t = 0

            i = randint(0, len(aster_imags)-1)
            aster = Asteroid(aster_imags[i], False)
            self.list.append(aster)
            self.n += 1

        self.t = t - self.aux


    
    
