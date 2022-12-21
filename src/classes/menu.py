import pygame.draw as pyd
import pygame.font as fon
from numpy import array
from numpy.linalg import norm
from pygame import K_ESCAPE, KEYDOWN

import utils.setup as sp
from classes.time import Counter


class Menu:
    def __init__(self):
        self.show = True
        self.exit_game = False
        self.color = (0,190,255)
        self.color_ol = (255,255,255)
        self.color_text = (0,0,0)
        self.pos_play = array([sp.WIN_WIDTH*0.5, sp.WIN_HEIGHT*0.35])
        self.pos_exit = array([sp.WIN_WIDTH*0.5, sp.WIN_HEIGHT*0.65])
        self.width = 150
        self.width_ol = 30
        fon.init()
        self.text = fon.SysFont('Calibri', 80, bold=True)
        self.text_surface_play = self.text.render('PLAY', True, self.color_text)
        self.text_surface_exit = self.text.render('EXIT', True, self.color_text)
        self.counter1 = Counter()
        self.counter2 = Counter()

    def draw(self, win):
        pyd.circle(win, self.color_ol, [self.pos_play[0]-self.text_surface_play.get_width()/2, self.pos_play[1]], 
            (self.width+self.width_ol)/2)
        pyd.circle(win, self.color_ol, [self.pos_play[0]+self.text_surface_play.get_width()/2, self.pos_play[1]], 
            (self.width+self.width_ol)/2)
        pyd.line(win, self.color_ol, [self.pos_play[0]-self.text_surface_play.get_width()/2, self.pos_play[1]], 
            [self.pos_play[0]+self.text_surface_play.get_width()/2, self.pos_play[1]], width=self.width+self.width_ol)
        pyd.circle(win, self.color, [self.pos_play[0]-self.text_surface_play.get_width()/2, self.pos_play[1]], self.width/2)
        pyd.circle(win, self.color, [self.pos_play[0]+self.text_surface_play.get_width()/2, self.pos_play[1]], self.width/2)
        pyd.line(win, self.color, [self.pos_play[0]-self.text_surface_play.get_width()/2, self.pos_play[1]], 
            [self.pos_play[0]+self.text_surface_play.get_width()/2, self.pos_play[1]], width=self.width)
  
        pyd.circle(win, self.color_ol, [self.pos_exit[0]-self.text_surface_exit.get_width()/2, self.pos_exit[1]], 
            (self.width+self.width_ol)/2)
        pyd.circle(win, self.color_ol, [self.pos_exit[0]+self.text_surface_exit.get_width()/2, self.pos_exit[1]], 
            (self.width+self.width_ol)/2)
        pyd.line(win, self.color_ol, [self.pos_exit[0]-self.text_surface_exit.get_width()/2, self.pos_exit[1]], 
            [self.pos_exit[0]+self.text_surface_exit.get_width()/2, self.pos_exit[1]], width=self.width+self.width_ol)
        pyd.circle(win, self.color, [self.pos_exit[0]-self.text_surface_exit.get_width()/2, self.pos_exit[1]], self.width/2)
        pyd.circle(win, self.color, [self.pos_exit[0]+self.text_surface_exit.get_width()/2, self.pos_exit[1]], self.width/2)
        pyd.line(win, self.color, [self.pos_exit[0]-self.text_surface_exit.get_width()/2, self.pos_exit[1]], 
            [self.pos_exit[0]+self.text_surface_exit.get_width()/2, self.pos_exit[1]], width=self.width)
    
        win.blit(self.text_surface_play, [sp.WIN_WIDTH*0.5-self.text_surface_play.get_width()/2, 
            sp.WIN_HEIGHT*0.35-self.text_surface_play.get_height()/2])
        win.blit(self.text_surface_exit, [sp.WIN_WIDTH*0.5-self.text_surface_exit.get_width()/2, 
            sp.WIN_HEIGHT*0.65-self.text_surface_exit.get_height()/2])
                
    def play(self, spcraft_pos):
        d = norm(self.pos_play-spcraft_pos)
        return d <= self.width/2*1.2

    def exit(self, spcraft_pos):
        d = norm(self.pos_exit-spcraft_pos)
        return d <= self.width/2*1.2

    def update(self, events, spcraft_pos, dt):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.show = True
                
        if self.counter1.counter((self.show and self.play(spcraft_pos)), sp.DT_HOLD, dt):
            self.show = False

        if self.counter2.counter((self.show and self.exit(spcraft_pos)), sp.DT_HOLD, dt):
            self.exit_game = True
