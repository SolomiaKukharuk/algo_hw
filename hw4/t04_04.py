from math import sin


def f(x):
    return sin(x)/x


def binary_con(f, c, a, b):
    l = a
    r = b
    m = l + (r-l)/2
    while m != l and m != r:
        if f(m) > c:
            l = m
        else:
            r = m
        m = l + (r-l)/2
    return l


if __name__=="__main__":
    res = binary_con(f, 1/3, 1.6, 3)
    print(res)
