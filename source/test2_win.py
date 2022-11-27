import os
import pickle
import random
import time
import pyautogui

import test_alpha.test_alpha1 as talpha

import neat
import pygame
import visualize
pygame.font.init()  # init font


def main(cap, hands, mp_hands, mp_drawing_styles, mp_drawing):
    WIN_WIDTH = 1800
    WIN_HEIGHT = 980
    FLOOR = 730
    #STAT_FONT = pygame.font.SysFont("comicsans", 50)
    #END_FONT = pygame.font.SysFont("comicsans", 70)
    DRAW_LINES = False

    bird_img = [pygame.transform.scale(pygame.image.load(os.path.join("source\pictures", "pic_1.png")), (100, 100) )]
    pipe_img  = pygame.transform.scale2x(pygame.image.load(os.path.join("source\pictures", "pic_4.png")))
    base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("source\pictures", "pic_3.png")))
    bg_img  = pygame.transform.scale2x(pygame.image.load(os.path.join("source\pictures", "pic_2.png")))


    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    class Bird:
        IMGS = bird_img

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.tilt = 0  # degrees to tilt
            self.tick_count = 0
            self.vel = 0
            self.height = self.y
            self.img_count = 0
            self.img = bird_img

        def draw(self, win):
            win.blit(bird_img[0], (self.x, self.y))

        def get_mask(self):
            return pygame.mask.from_surface(self.img)



    #window
    def draw_window(win, bird):
        win.blit(bg_img, (0,0))
        bird.draw(win)

        pygame.display.update()


    #loop game
    while True:
        #x, y = pygame.mouse.get_pos()
        #xy = talpha.test_3(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
        x, y = talpha.test_3(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
        #print("xy", type(xy))
        if x >= 0 and x <= 1:
            x1 = x*500
            y1 = y*500
        else:
            x1 = 200
            y1 = 200


        #x1, y1 = pyautogui.position()
        #time.sleep(1)
        print("x1", x1, "y1", y1)

        bird1 = Bird(x1, y1)
        draw_window(WIN, bird1)

"""
if __name__ == "__main__":
    main()
"""

