import math

def fun1(x):
    return (x % 6)**2 % 7 - math.sin(x)


def main():
    min = max = 0
    xmin = xmax = 0

    for x in range(1, 100):
        val = fun1(x)
        print("x is: %3d, value is: %.3f" % (x, val))
        if val < min:
            min = val
            xmin = x

        if val > max:
            max = val
            xmax = x

    print("xmin: %3d; min: %.3f" % (xmin, min))
    print("xmax: %3d; max: %.3f" % (xmax, max))

if __name__ == '__main__':
    main()
