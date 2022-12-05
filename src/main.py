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

    #open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    with mp_hands.Hands(
        max_num_hands = 1,
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        
        #load images
        spcft, aster, bg, exp = img.load_imag()
        
        spacecraft = Spacecraft(0.5, 0.5, spcft)
        window = Window(sp.WIN_WIDTH, sp.WIN_HEIGHT, bg)
        window.update(spacecraft)
        
        ListCoord(sp.N_FILTER)

        #game loop
        while True:
            vect = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)

            """
            print("vect=", x)
            print("type", type(x))

            # update the list of past values
            past_values.append((x, y, z))
            # remove the oldest value from the list if the list is longer than N
            if len(past_values) > N:
                past_values.pop(0)
            # compute the weighted average of the current and past positions
            # to get the smoothed position of the bird
            x_smooth = sum([x * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
            y_smooth = sum([y * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
            z_smooth = sum([z * (i+1) for i, (x, y, z) in enumerate(past_values)]) / weighted_avg_denominator
            # update the position of the bird using the smoothed coordinates
            #x, y, z = x_smooth, y_smooth, z_smooth
            
            
            
            x1 = (-x_smooth+1)*sp.WIN_WIDTH
            y1 = y_smooth*sp.WIN_HEIGHT
            scaled_spcft_img = pygame.transform.scale(spcft, (sp.SPCRFT_W0*(0.7-z_smooth*3), sp.SPCRFT_H0*(0.7-z_smooth*3)))
            """
            
            
            """
            if x >= 0 and x <= 1:
                x1 = (1-x)*sp.WIN_WIDTH
                y1 = y*sp.WIN_HEIGHT
                z1 = z
            else:
                x1 = 200
                y1 = 200
                z1 = 1
            """

            """
            #from mouse cursor
            x1, y1 = pyautogui.position()
            print("x1", x1, "y1", y1)
            z1 = 1
            if x1 >= 0 and x1 <= sp.WIN_WIDTH:
                x2 = x1
                y2 = y1
            else:
                x2 = 200
                y2 = 200
                
            """

            #aster_1 = 
            spacecraft.update(vect[0], vect[1], vect[2])
            window.update(spacecraft)

            """
            to-do
            if
                break
            """


            














if __name__ == "__main__":
    #main()


    aa = ListCoord(5)
    print(type(aa))
    print(aa)
    
