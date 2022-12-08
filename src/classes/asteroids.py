import utils.setup as sp
from random import uniform, randint
from pygame.transform import rotate, rotozoom
from math import cos, sin, radians
from numpy import array

class Asteroid:
    def __init__(self, imag, commet): #(image, True=commet/Falsenot commet)
        self.f = uniform(sp.ASTER_F1, 1)
        self.w = sp.ASTER_W0_H0*self.f
        self.h = sp.ASTER_W0_H0*self.f
        self.x = sp.WIN_WIDTH*(1+sp.ASTER_X0)
        self.y = uniform( sp.WIN_HEIGHT*(1-sp.ASTER_Y0)/2, sp.WIN_HEIGHT*((1+sp.ASTER_Y0)/2) )
        self.vel = uniform(sp.ASTER_VEL_MIN, sp.ASTER_VEL_MAX)
        self.alpha = uniform(-sp.ASTER_ALPHA, sp.ASTER_ALPHA)
        self.commet = commet
        self.beta = 0
        self.imag0 = rotozoom(imag, -self.alpha, self.f)
        self.imag = self.imag0
        self.life = True

        self.init_commet()
        
    def init_commet(self):
        if self.commet:
            self.vrot = 0
            self.r = min(self.w/2, self.h/2) * sp.HITBOX_COMMET
        else:
            self.vrot = uniform(-sp.ASTER_VROT_RANGE, sp.ASTER_VROT_RANGE)
            self.r = min(self.w/2, self.h/2) * sp.HITBOX_FACTOR

    def draw(self, win):
        win.blit(self.imag, self.get_pos_draw())
    
    def end_life(self):
        a = self.x <= -sp.END_ASTER_LIFE
        b = self.y <= -sp.END_ASTER_LIFE
        c = self.y >= sp.WIN_HEIGHT + sp.END_ASTER_LIFE

        return not(a or b or c)

    def get_pos_draw(self): #return [x, y] image's center
        return array([self.x-self.w/2, self.y-self.h/2])

    def update(self, dt):
        if not(self.commet):
            self.imag = rotate(self.imag0, self.vrot*dt + self.beta)
            self.beta = self.vrot*dt + self.beta

        self.w = self.imag.get_width()
        self.h = self.imag.get_height()
        self.x = self.x - self.vel*dt*cos(radians(self.alpha))
        self.y = self.y - self.vel*dt*sin(radians(self.alpha))
        self.life = self.end_life()


class ListAsteroids:
    def __init__(self, imags):
        self.list = []
        self.imags = imags
        self.n = 0
        self.n_c = 0   #n total creations

    def draw(self, win):
        for i in range(self.n):
            self.list[i].draw(win)

    def insert_element(self, elem):
        self.list.append(elem)
        self.n += 1

    def pop_element(self):
        for i in range(self.n):
            if not(self.list[i].life):
                self.list.pop(i)
                self.n -= 1
                break

    def update(self, t, dt):
        if t >= sp.ASTER_DT*self.n_c:
            self.n_c += 1
            i = randint(0, len(self.imags)-1)
            self.insert_element( Asteroid(self.imags[i], i==0) ) #i=0 is a commet

        for i in range(self.n):
            self.list[i].update(dt)
            
        self.pop_element()
            
    def get_pos_list(self):
        list = []
        for i in range(self.n):
            list.append([self.list[i].x, self.list[i].y, self.list[i].r])

        return list
