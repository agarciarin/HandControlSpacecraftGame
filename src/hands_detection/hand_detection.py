import cv2
from numpy import array

import utils.setup as sp


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

class ListCoord:
    def __init__(self, n_max):
        self.list = []
        self.n = 0
        self.n_max = n_max

    def insert(self, coord):
        self.list.append(coord)
        self.n += 1

    def pop_last_element(self):
        self.list.pop(0)
        self.n -= 1
        
    def filter(self):
        avg_denom = sum(range(1, self.n+1))

        x_smooth = sum( [x * (i+1) for i, (x, y, z) in enumerate(self.list)] ) / avg_denom
        y_smooth = sum( [y * (i+1) for i, (x, y, z) in enumerate(self.list)] ) / avg_denom
        z_smooth = sum( [z * (i+1) for i, (x, y, z) in enumerate(self.list)] ) / avg_denom
        
        return [x_smooth, y_smooth, z_smooth]
    
