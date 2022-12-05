



class Window:

    def __init__(self, h, w, imag):
        self.h = h
        self.w = w
        self.bg = imag

    def draw(self, win, spcft):
        win.blit(self.bg, (0,0))
        spcft.draw(win)



