#Simply test functions to learn it behavior

def main():
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



    

if __name__ == "__main__":
    main()