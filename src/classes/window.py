import pygame

class Window:
    def __init__(self, h, w, imag):
        self.h = h
        self.w = w
        self.bg = imag
        self.window = pygame.display.set_mode((h, w))
        
        pygame.display.set_caption("Spacecraft game")

    def blit(self, imag, vect):
        self.window.blit(imag, vect)
    
    def draw(self, spcft):
        self.blit(self.bg, (0,0))
        spcft.draw(self.window)

    def update(self, spacecraft):
        self.draw(spacecraft)
        pygame.display.update()
