from numpy import array


#Define setup variables

#Window
WIN_WIDTH = 1800    #(px)
WIN_HEIGHT = 900    #(px)
FPS = 60

#Menu
DT_HOLD = 2 #(s) PLAY/EXIT menu

#Filtering camera input
N_FILTER = 10           #Nº samples

#Spacecraft
SPCRAFT_W0 = 800        #(px)    
SPCRAFT_H0 = 800        #(px)
SPCRAFT_Y_CORR = 1.5    #[1-2] Hand margin detection
SPCRAFT_POS0 = array([0.8, 0.5/SPCRAFT_Y_CORR, -0.1])
SPCRAFT_F1 = 6          #Factor1 = max imag size
SPCRAFT_F2 = 0.1        #Factor2 = avoid loss resolution
SPCRAFT_SHIELD0 = 5
SPCRAFT_DAMAGE_FACTOR = 1
SPCRAFT_REPAIR_FACTOR = 0.05 #[0-SPCRAFT_DAMAGE_FACTOR)

#Asteroids
END_ASTER_LIFE = 500    #(px)
ASTER_W0_H0 = 200       #(px)
ASTER_F1 = 0.5          #(0-1] % of ASTER_W0_H0 = min/max value of images size
ASTER_X0 = 0.1          #[0.1 - 0.5] where asteroids appear
ASTER_Y0 = 0.8          #[0.1 - 1] where asteroids appear
ASTER_VEL_MIN = 200     #(px/s) 
ASTER_VEL_MAX = 1000    #(px/s)
ASTER_ALPHA = 15        #(deg)
ASTER_VROT_RANGE = 500  #(deg/s)

#Asteroids List
ASTER_DT = 0.5          #(s) time between creation of asteroids

#Hitbox
HITBOX_FACTOR = 0.4     # % ratio hitbox
HITBOX_COMMET = 0.2     # % ratio hitbox for commet 
