from numpy import array
from numpy.linalg import norm
from pygame.transform import scale

import utils.setup as sp


class Spacecraft:
    def __init__(self, x, y, imag):
        self.f = sp.SPCRAFT_F2
        self.w = sp.SPCRAFT_W0 * self.f
        self.h = sp.SPCRAFT_H0 * self.f
        self.x = (1-x)*sp.WIN_WIDTH
        self.y = y*sp.WIN_HEIGHT*sp.SPCRAFT_Y_CORR
        self.z = 1
        self.imag0 = imag 
        self.imag = imag 
        self.r = min(self.w/2, self.h/2) * sp.HITBOX_FACTOR
        self.shield = sp.SPCRAFT_SHIELD0
        self.damaged = False

    def collision(self, list_pos):
        colli = False
        for i in range(len(list_pos)):
            coord = list_pos[i]
            d = norm(array([self.x, self.y])-array([coord[0], coord[1]]))
            if d <= (self.r + coord[2]):
                colli = True
                break
            else:
                colli = False
        return colli

    def damage(self, list_pos, dt):
        if self.collision(list_pos):
            self.shield -= sp.SPCRAFT_DAMAGE_FACTOR*dt

    def draw(self, win):
        win.blit(self.imag, self.get_pos_draw())

    def get_pos_draw(self): #return [x, y] image's center
        return array([self.x-self.w/2, self.y-self.h/2])

    def get_pos(self):
        return array([self.x, self.y])    
    
    def limits(self):
        if self.x <= self.w/2:
            self.x = self.w/2
        elif self.x >= sp.WIN_WIDTH-self.w/2:
            self.x = sp.WIN_WIDTH-self.w/2

        if self.y <= self.h/2:
            self.y = self.h/2
        elif self.y >= sp.WIN_HEIGHT-self.h/2:
            self.y = sp.WIN_HEIGHT-self.h/2

    def repair_damage(self, dt):
        if self.shield <= sp.SPCRAFT_SHIELD0:
            self.shield += sp.SPCRAFT_REPAIR_FACTOR*dt

    def update(self, x, y, z, list_pos, dt):
        self.z = z
        self.f = abs((-(sp.SPCRAFT_F1-1)*z/0.7 + 1)*sp.SPCRAFT_F2)
        self.w = sp.SPCRAFT_W0 * self.f
        self.h = sp.SPCRAFT_H0 * self.f
        self.x = (1-x)*sp.WIN_WIDTH
        self.y = y*sp.WIN_HEIGHT*sp.SPCRAFT_Y_CORR
        self.imag = scale(self.imag0, (self.w, self.h))
        self.r = max(self.w/2, self.h/2)
        self.damaged = (self.shield <= 0)
       
        self.limits()
        self.damage(list_pos, dt)
        self.repair_damage(dt)
    