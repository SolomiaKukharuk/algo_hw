from math import sqrt


def f(x):
    return (x**3 + x + 1)


def binary_con(f, c, a, b):
    l = a
    r = b
    m = l + (r-l)/2
    while m != l and m != r:
        if f(m) < c:
            l = m
        else:
            r = m
        m = l + (r-l)/2
    return l


if __name__=="__main__":
    res = binary_con(f, 5, 0, 10)
    print(res)
