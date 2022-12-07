import utils.setup as sp
from random import uniform, randint
import pygame.transform as trans

class Asteroid:
    def __init__(self, imag, rotation): #(image, True/False)
        self.w = randint(sp.ASTER_F1*sp.ASTER_W0_H0, sp.ASTER_W0_H0)
        self.h = self.w
        #self.x = sp.WIN_WIDTH*(1+sp.ASTER_X0) - self.w/2
        self.x = 1000 
        self.y = uniform( sp.WIN_HEIGHT*(1-sp.ASTER_Y0)/2, sp.WIN_HEIGHT*((1+sp.ASTER_Y0)/2) ) - self.h/2
        self.vel = uniform(sp.ASTER_VEL_MIN, sp.ASTER_VEL_MAX)
        self.alpha = uniform(-sp.ASTER_ALPHA, sp.ASTER_ALPHA)
        self.rot = rotation
        self.vrot = uniform(sp.ASTER_VROT_MIN, sp.ASTER_VROT_MAX)
        self.imag = trans.scale(imag, (self.w, self.h))
        self.life = True

    def draw(self, win):
        win.blit(self.imag, [self.x, self.y])

    def update(self):
        #update in function of time
        return self.end_life()
        
    def end_life(self):
        a = self.x <= -sp.END_ASTER_LIFE
        b = self.y <= -sp.END_ASTER_LIFE
        c = self.y >= sp.WIN_HEIGHT + sp.END_ASTER_LIFE

        print(a and b and c) #for check
        return a and b and c


class ListAsteroids:
    def __init__(self):
        self.list = []
