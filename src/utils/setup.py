from numpy import array


#Define setup variables

WIN_WIDTH = 1800
WIN_HEIGHT = 900
FPS = 60

SPCRAFT_W0 = 600
SPCRAFT_H0 = 600

#Spacecraft initial position
SPCRAFT_POS0 = array([0.8, 0.5, 0])
SPCRAFT_F1 = 8      #Resize factor1
SPCRAFT_F2 = 0.15   #Resize factor2

#Filtering
N_FILTER = 8 
