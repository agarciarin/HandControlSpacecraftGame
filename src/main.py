# Minigame controled by hand gesture

import cv2
import mediapipe as mp
import pyautogui
import pygame
import time

import utils.load_images as img
import utils.setup as sp
from classes.window import Window
from classes.spacecraft import Spacecraft
from classes.asteroids import ListAsteroids
from classes.time import Time
from classes.scoreboard import Scoreboard
from hands_detection.hand_detection import hand_cap, ListCoord

#Delete
import numpy as np


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
        clock = pygame.time.Clock()

        #Load images
        sp_imag, aster_imags, bg_imag, exp_imag = img.load_imag()
        
        window = Window(sp.WIN_WIDTH, sp.WIN_HEIGHT, bg_imag)
        spacecraft = Spacecraft(0.5, 0.5, sp_imag)
        explosion = Spacecraft(0.5, 0.5, exp_imag)
        listAster = ListAsteroids(aster_imags)
        scoreboard = Scoreboard()
        
        list = ListCoord(sp.N_FILTER)

        t = Time(time.time())

        #Game loop
        while True:
            pygame.event.get()
            clock.tick(sp.FPS)
            t.update(time.time())

            #coord0 = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
            
            ###BEGIN_ControlMouse
            aux = pyautogui.position()
            coord0 = np.array([1-aux[0]/1920, aux[1]/1080, -0.1])
            ###EEND_ControlMouse

            list.insert(coord0)
            if list.n > list.n_max:
                list.pop_last_element()
            
            coord_smooth = list.filter()
            if spacecraft.shield <= 0:
                explosion.update(last_coord[0], last_coord[1], last_coord[2], exp_imag, [], 0)
                window.update(explosion, listAster, scoreboard)
                time.sleep(3)
                break
            else:
                spacecraft.update(coord_smooth[0], coord_smooth[1], coord_smooth[2], sp_imag, listAster.get_pos_list(), t.get_dt())
                last_coord = coord_smooth
                listAster.update(t.get_t(), t.get_dt())
                scoreboard.update(spacecraft.shield, t.get_t())
                window.update(spacecraft, listAster, scoreboard)

                #print("Shield", spacecraft.shield)
                #print("Time", t.get_t())

            #scoreboard.draw_score(window.window)

            """
            to-do:
            -if condition finish game or escape
                break

            -if colision finish game
            -score marker on screen
            -init menu
            -maybe: start game when wave hand or similar
            -maybe: customize z coordinate filter -> smoother
            """


if __name__ == "__main__":
    main()
