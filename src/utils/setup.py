from numpy import array


#Define setup variables

#Window
WIN_WIDTH = 1800
WIN_HEIGHT = 900
FPS = 60

#Spacecraft initial position
SPCRAFT_W0 = 800
SPCRAFT_H0 = 800
SPCRAFT_POS0 = array([0.8, 0.5, -0.1 ])
SPCRAFT_F1 = 6     #Factor1 = max imag size
SPCRAFT_F2 = 0.1   #Factor2 = avoid loss resolution
SPCRAFT_SHIELD0 = 5
SPCRAFT_DAMAGE_FACTOR = 1
SPCRAFT_REPAIR_FACTOR = 0.05 #[0-SPCRAFT_DAMAGE_FACTOR)

#Filtering
N_FILTER = 10 

#Asteroids
END_ASTER_LIFE = 500
ASTER_W0_H0 = 600
ASTER_F1 = 0.1 # % of ASTER_W0_H0 = min value of images size
ASTER_X0 = 0.1 #[0.1 - 0.5]
ASTER_Y0 = 0.5 #[0.1 - 1]
ASTER_VEL_MIN = 200 
ASTER_VEL_MAX = 800
ASTER_ALPHA = 20 #(deg)
ASTER_VROT_RANGE = 500 #(deg/s)

#Asteroids List
ASTER_DT = 0.6 #(s) time between creation of asteroids

#Hitbox
HITBOX_FACTOR = 0.7   # % ratio hitbox
HITBOX_COMMET = 0.2  
