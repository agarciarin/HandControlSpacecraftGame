import pygame


class Window:
    def __init__(self, h, w, imag):
        self.h = h
        self.w = w
        self.bg = imag
        self.window = pygame.display.set_mode([h, w])
    
        pygame.display.set_caption("Hand Control Spacecraft Game")
    
    def blit_(self, imag, vect):
        self.window.blit(imag, vect)
    
    def draw(self, spcft, aster):
        self.blit_(self.bg, [0,0])
        aster.draw(self.window)
        spcft.draw(self.window)

    def update(self, spacecraft, asteroids):
        self.draw(spacecraft, asteroids)
        pygame.display.update()
