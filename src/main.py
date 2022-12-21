# Minigame controled by hand gesture

import time

import cv2
import mediapipe as mp
import pyautogui
import pygame
from numpy import array

import utils.load_images as img
import utils.setup as sp
from classes.asteroids import ListAsteroids
from classes.game import Game
from classes.menu import Menu
from classes.scoreboard import Scoreboard
from classes.spacecraft import Spacecraft
from classes.time import Time
from classes.window import Window
from hands_detection.hand_detection import ListCoord, hand_cap


def delete_objects(list_objs):
    for i in range(len(list_objs)):
        del list_objs[0]
    del list_objs


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
        menu = Menu()
        game = Game()

        #Main loop
        while not menu.exit_game:

            #Load images and Objects
            sp_imag, aster_imags, bg_imag, exp_imag = img.load_imag()
            window = Window(sp.WIN_WIDTH, sp.WIN_HEIGHT, bg_imag)
            spacecraft = Spacecraft(0.5, 0.5, sp_imag)
            explosion = Spacecraft(0.5, 0.5, exp_imag)
            listAster = ListAsteroids(aster_imags)
            scoreboard = Scoreboard()
            list = ListCoord(sp.N_FILTER)
            t = Time(time.time())

            #Game loop
            while not menu.exit_game:
                events = pygame.event.get()
                clock.tick(sp.FPS)
                t.update(time.time(), menu.show)
                
                coord0 = hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)
                ###BEGIN_ControlMouse
                #aux = pyautogui.position()
                #coord0 = array([1-aux[0]/1920, aux[1]/1080/sp.SPCRAFT_Y_CORR, -0.1])
                ###EEND_ControlMouse

                #Filter input
                list.insert(coord0)
                if list.n > list.n_max:
                    list.pop_last_element()
                coord_smooth = list.filter()
                        
                #Update
                spacecraft.update(coord_smooth[0], coord_smooth[1], coord_smooth[2], listAster.get_pos_list(), t.dt)
                window.update(spacecraft, listAster, scoreboard, menu)
                menu.update(events, spacecraft.get_pos(), t.dt)

                if not menu.show:
                    if spacecraft.damaged:
                        explosion.update(last_coord[0], last_coord[1], last_coord[2], [], 0)
                        window.update(explosion, listAster, scoreboard, menu)
                        time.sleep(1)
                        menu.show = True
                        break
                    else:
                        last_coord = coord_smooth
                        listAster.update(t.tg, t.dt)
                        scoreboard.update(spacecraft.shield, t.tg)
            
            game.update()
            game.print_game(scoreboard)
            delete_objects([window, spacecraft, explosion, listAster, scoreboard, list, t, 
                sp_imag, aster_imags, bg_imag, exp_imag])

        game.print_games()
        

if __name__ == "__main__":
    main()
