import cv2
import utils.setup as sp
from numpy import array, empty, ndarray


def hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing):
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")

    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    """
    # Draw the hand annotations on the image and show camera window
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    """

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            return array([hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y, hand_landmarks.landmark[8].z])

    else:
        return sp.SPCRAFT_POS0
"""
class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coord(self):
        return array([self.x, self.y, self.z])
"""
class ListCoord:
    def __init__(self, N):
        self.list = empty([N], dtype=ndarray)

    def update(self):
        self

    def filter(coord):
        
        return 0
    
