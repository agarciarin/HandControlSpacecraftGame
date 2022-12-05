import cv2
import mediapipe as mp
import pygame

import utils.setup as sp
import utils.load_images as img
from hands_detection.hand_detect import hand_cap
import class_spacecraft.spacecraft as spcraft
import class_window.window as windo



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
        
        WIN = pygame.display.set_mode((sp.WIN_WIDTH, sp.WIN_HEIGHT))
        pygame.display.set_caption("Spacecraft game")


        #game loop
        while True:
            vect = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)

            print("vect=", vect)
            print("type", type(vect))
            """
            if x >= 0 and x <= 1:
                x1 = (1-x)*sp.WIN_WIDTH
                y1 = y*sp.WIN_HEIGHT
            else:
                x1 = 200
                y1 = 200
           
            spcft_1 = spcraft(vect[0], vect[1], vect[2], spcft)
            windo.draw(WIN, spcft_1)
            """














if __name__ == "__main__":
    main()



