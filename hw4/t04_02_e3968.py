from math import sqrt


def f(x):
    return (x**2 + sqrt(x))


if __name__=="__main__":
    c = float(input())
    l = 0
    r = 10**10
    m = l + (r-l)/2
    while m != l and m != r:
        if f(m) < c:
            l = m
        else:
            r = m
        m = l + (r-l)/2

    print(l)
    