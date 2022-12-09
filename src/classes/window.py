from pygame.display import set_mode, set_caption, update


class Window:
    def __init__(self, h, w, imag):
        self.h = h
        self.w = w
        self.bg = imag
        self.window = set_mode([h, w])
    
        set_caption("Hand Control Spacecraft Game")
    
    def blit_(self, imag, vect):
        self.window.blit(imag, vect)
    
    def draw(self, spcft, aster, score, menu):
        self.blit_(self.bg, [0,0])
        aster.draw(self.window)
        if menu.show:
            menu.draw(self.window)
        spcft.draw(self.window)
        score.draw(self.window)

    def update(self, spacecraft, asteroids, scoreboard, menu):
        self.draw(spacecraft, asteroids, scoreboard, menu)
        update()
