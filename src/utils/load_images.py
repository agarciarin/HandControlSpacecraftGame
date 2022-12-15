from os.path import join
from pygame.surface import Surface
from pygame.transform import scale
from pygame.image import load
from numpy import empty
from random import randint
from utils.setup import WIN_HEIGHT, WIN_WIDTH, SPCRAFT_W0, SPCRAFT_H0, ASTER_W0_H0, COMMET_W0_H0



# load images: spacecrafts, asteroids, background, explosion
def load_imag():     
    
    N_spcraft = 5
    N_bg = 14
    N_aster = 9

    #only return one spacecraft and one background
    n_spcraft = randint(1, N_spcraft)
    n_bg = randint(1, N_bg)

    spacecraft_imag = scale( load(join("doc/images/spacecraft/spa_" + str(n_spcraft) + ".png")), (SPCRAFT_W0, SPCRAFT_H0) )
    bg_imag  = scale( load(join("doc/images/background/bg_" + str(n_bg) + ".jpg")), (WIN_WIDTH, WIN_HEIGHT) )
    exp_imag = scale( load(join("doc/images/spacecraft/explosion.png")), (SPCRAFT_W0, SPCRAFT_H0) )
    
    aster_imag = empty([N_aster], dtype=Surface)
    aster_imag[0] = scale( load(join("doc/images/asteroid/asteroid_" + str(1) + ".png")), (COMMET_W0_H0, COMMET_W0_H0) ) #load commet
    for i in range(N_aster-1):
        aster_imag[i+1] = scale( load(join("doc/images/asteroid/asteroid_" + str(i+2) + ".png")), (ASTER_W0_H0, ASTER_W0_H0) )
  
    return spacecraft_imag, aster_imag, bg_imag, exp_imag
