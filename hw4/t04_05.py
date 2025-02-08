def f(x):
    return (x**3 + 4 * x ** 2 + x - 6)


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
    return r


if __name__=="__main__":
    res = binary_con(f, 0, 0, 2)
    print(res)
