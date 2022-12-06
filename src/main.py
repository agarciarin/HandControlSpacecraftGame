import cv2
import mediapipe as mp
import pyautogui
import pygame
import numpy as np

import utils.load_images as img
import utils.setup as sp
from classes.spacecraft import Spacecraft
from classes.window import Window
from hands_detection.hand_detect import hand_cap, ListCoord



def main():

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    #Open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    with mp_hands.Hands(
        max_num_hands = 1,
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        
        pygame.init() # Initializing PyGame

        #Load images
        sp_imag, aster_imags, bg_imag, exp_imag = img.load_imag()
        
        spacecraft = Spacecraft(0.5, 0.5, sp_imag)
        window = Window(sp.WIN_WIDTH, sp.WIN_HEIGHT, bg_imag)
        
        #ListCoord(sp.N_FILTER)


        #Game loop
        while True:
            pygame.event.get()
            vect = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
            
            
            ###BEGIN_ControlMouse
            aux = pyautogui.position()
            #vect = np.array([1-aux[0]/1920, aux[1]/1080, -0.1])
            ###EEND_ControlMouse
            #print(vect)

            window.update(spacecraft)
            #aster_1 = 
            spacecraft.update(vect[0], vect[1], vect[2])
            #window.update(spacecraft)
        



            """
            to-do
            if condition finish game or escape
                break
            """


            














if __name__ == "__main__":
    main()

    """
    aa = ListCoord(5)
    print(type(aa))
    print(aa)
    """
