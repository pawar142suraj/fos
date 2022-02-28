import math


def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


if __name__ == '__main__':

    y = float(input("Enter the value of y\n"))

    # if type(y) == float:
    #     maxx = 10
    #     minn =1
    # elif type(y) == int:
    if y > 2 and y < 1000000000:
        maxx = 9.0
        minn = 1.0
        precision = 0.000001
        prev_guess = 0
        new_guess = (maxx + minn) / 2
        while diff(new_guess, prev_guess) > precision:
            if math.pow(new_guess, new_guess) > y:
                maxx = new_guess
                prev_guess = maxx
                new_guess = (new_guess - minn) / 2


            elif math.pow(new_guess, new_guess) < y:

                minn = new_guess
                prev_guess = new_guess
                new_guess = (new_guess + maxx) / 2

            else:
                prev_guess = new_guess

    else:
        print("Enter y value between (2,1000000000)")

    print("The value of x is {:6.7}f".format(new_guess))







