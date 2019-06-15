import math

def fun2(x):
    return -x**4 + 1000 * x**3 - 20 * x**2 + 4*x - 6


def main():
    max = xmax = 0

    for x in range(1, 1000):
        val = fun2(x)
        print("x is: %3d, value is: %.3f" % (x, val))

        if val > max:
            max = val
            xmax = x

    print("xmax: %3d; max: %.3f" % (xmax, max))

if __name__ == '__main__':
    main()