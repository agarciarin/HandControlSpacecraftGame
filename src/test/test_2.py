#Simply test functions to learn it behavior
import pyautogui
import numpy as np
import time
from math import dist
from numpy.linalg import norm

def main_test1():
    """
    N = 2
    past_values = [[0.5, 0.6, -0.1], [0.45, 0.55, -0.05]]
    print("sss", past_values[1])
    weighted_avg_denominator = sum(range(1, N+1))

    x, y, z = 0.55, 0.65, -0.15

    x_smooth = sum( [x * (i+1) for i, (x, y, z) in enumerate(past_values)])/weighted_avg_denominator
        
    print("x_smooth=", x_smooth)
    print("x=", x)
    """
    """
    N = 2
    weighted_avg_denominator = sum(range(1, N+1))
    print(weighted_avg_denominator)
    past_values = [np.array([0.5, 0.6, -0.1]), np.array([0.55, 0.55, -0.05])]


    aa = [x * (i+1) for i, (x,y,z) in enumerate(past_values)]
    #aa = [x * (i+1) for i, x in enumerate(past_values)]
    print("aa", aa)
    bb = sum(aa)
    print("bb", bb)
    cc = bb/weighted_avg_denominator
    print("cc", cc)
    """
    """
    N = 3
    weighted_avg_denominator = sum(range(1, N+1))
    print(weighted_avg_denominator)
    """

def main_test2():

    while True:
        time.sleep(1)
        aux = pyautogui.position()
        coord0 = np.array([1-aux[0]/1920, aux[1]/1080, -0.1])

        a = coord0[0] <= 1.1
        b = coord0[1] <= 1.1

        print(coord0)
        print(a)
        print(b)
        print(a and b)

def main_test3():
    N_aster = 7
    for i in range(N_aster):
        print(i)

def main_test4():
    i = 0
    print(i == 0)

    for i in range(0):
        print(i)


def main_test5():
    a = [2, 5]
    b = [5, 1]
    c = dist(a,b)
    cc = norm(a,b)
    print(c)
    print(cc)

def  main_test6():
    pos = [5, 6]
    print(pos)

    pos[1] = pos[1]*10
    print(pos)



if __name__ == "__main__":
    #main_test1()
    #main_test2()
    #main_test3()
    #main_test4()
    #main_test5()
    main_test6()
