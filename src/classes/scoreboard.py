import utils.setup as sp
import pygame.draw as pyd
import pygame.font as fon


class Scoreboard:
    def __init__(self):
        self.shield = sp.SPCRAFT_SHIELD0
        self.score = 0
        self.aux = 0 
        self.color = (50,255,50)
        self.color_ol = (255,255,255)
        self.pos_low = [sp.WIN_WIDTH*0.03, sp.WIN_HEIGHT*0.8]
        self.pos_high = [sp.WIN_WIDTH*0.03, sp.WIN_HEIGHT*0.2]
        self.width = 50
        self.width_ol = 10
        fon.init()
        self.text = fon.SysFont('Comic Sans MS', 50, bold=True)
        self.text_surface = self.text.render('Score: '+str(self.score), True, self.color)


    def draw(self, win):
        pyd.circle(win, self.color_ol, self.pos_low, (self.width+self.width_ol)/2)
        pyd.circle(win, self.color_ol, self.pos_high, (self.width+self.width_ol)/2)
        pyd.line(win, self.color_ol, self.pos_low, self.pos_high, width=self.width+self.width_ol)

        pyd.circle(win, self.color, self.pos_low, self.width/2)
        pyd.circle(win, self.color, self.pos_high, self.width/2)
        pyd.line(win, self.color, self.pos_low, self.pos_high, width=self.width)
    
        win.blit(self.text_surface, [50, sp.WIN_HEIGHT*0.85])

    def update(self, shield, t):
        self.shield = shield/sp.SPCRAFT_SHIELD0
        self.pos_high[1] = sp.WIN_HEIGHT*0.8-(sp.WIN_HEIGHT*0.6)*self.shield
        
        #score colors
        if self.shield <= 0.1:
            self.color = (255,0,0)
        elif self.shield <= 0.5:
            self.color = (255,130,0)
        else:
            self.color = (50,255,50)

        #score marker
        if t >= 0.08*self.aux:
            self.aux += 1
            self.score = int(t*100)
        
        self.text_surface = self.text.render('Score: '+str(self.score), True, self.color)
