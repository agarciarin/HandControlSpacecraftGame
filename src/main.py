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

        N = 5
        past_values = []
        weighted_avg_denominator = sum(range(1, N+1))

        #game loop
        while True:
            x, y, z = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)

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
            if x >= 0 and x <= 1:
                x1 = (1-x)*sp.WIN_WIDTH
                y1 = y*sp.WIN_HEIGHT
            else:
                x1 = 200
                y1 = 200
            """
           

            spcft_1 = spcraft(x1, y1, scaled_spcft_img)
            #aster_1 = 

            windo.draw(WIN, spcft_1)
            














if __name__ == "__main__":
    main()



