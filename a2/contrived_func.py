import math


def contrived_func(val):

    a = val + math.sqrt(abs(val*3)) >= 23
    b = val ** 3 % 2 != 0
    c = val * 6 - 14 < 107
    d = val ** 3 < 0

    if a or b:
        if (a and b) or (b and c) and d:
            print("Triggered first conditional")
        else:
            print("Triggered second conditional")
    else:
        if (a or b) or (b or c):
            print("Triggered third conditional")
        else:
            print("Triggered fourth conditional")

    if a and b:
        print("Triggered fifth conditional")
    else:
        print("Triggered sixth conditional")
