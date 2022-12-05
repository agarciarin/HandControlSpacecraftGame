
import pygame
import utils.setup as sp


class Spacecraft:

    def __init__(self, x, y, imag):
        self.x = x
        self.y = y
        self.z = 1
        self.h = sp.SPCRFT_H0
        self.w = sp.SPCRFT_W0
        self.img = imag

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


def draw(self, win, spcft):
    win.blit(self.bg, (0,0))
    spcft.draw(win)

    pygame.display.update()












