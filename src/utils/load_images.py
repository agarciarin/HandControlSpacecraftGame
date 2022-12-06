import pygame
import os
from numpy import empty
from random import randint
from utils.setup import WIN_HEIGHT, WIN_WIDTH, SPCRAFT_W0, SPCRAFT_H0



# load images: spacecrafts, asteroids, background, explosion
def load_imag():     
    
    N_spcraft = 5
    N_bg = 14
    N_aster = 7

    #only return one spacecraft and one background
    n_spcraft = randint(1, N_spcraft)
    n_bg = randint(1, N_bg)

    aster_imag = empty([N_aster], dtype=pygame.Surface)

    spacecraft_imag = pygame.transform.scale( pygame.image.load(os.path.join("doc/images/spacecraft/spa_" + str(n_spcraft) + ".png")), (SPCRAFT_W0, SPCRAFT_H0) )
    bg_imag  = pygame.transform.scale( pygame.image.load(os.path.join("doc/images/background/bg_" + str(n_bg) + ".jpg")), (WIN_WIDTH, WIN_HEIGHT) )
    exp_imag = pygame.transform.scale( pygame.image.load(os.path.join("doc/images/spacecraft/explosion.png")), (SPCRAFT_W0, SPCRAFT_H0) )
    aster_imag[0] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_1.png"))
    aster_imag[1] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_2.png"))
    aster_imag[2] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_3.png"))
    aster_imag[3] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_4.png"))
    aster_imag[4] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_5.png"))
    aster_imag[5] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_6.png"))
    aster_imag[6] = pygame.image.load(os.path.join("doc/images/asteroid/asteroid_7.png"))
    
    return spacecraft_imag, aster_imag, bg_imag, exp_imag
