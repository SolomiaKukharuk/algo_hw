def a(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def b(n):
    summ = 0                     #O(1)
    for i in range(1, n + 1):    #O(n)
        i *= i                   #O(1)
        summ += i                #O(1)
    return summ                  #O(1) => загальна складність O(n)

def c(n, a):
    s = 0                  # O(1)
    for i in range(n+1):   # O(n)
        s += a**i          # O(1), якщо a - константа
    return s               # O(1)  => загальна складність O(n)

def d(n):
    s = 0                 # O(1)
    for _ in range(n):    # O(n)
        s += n**n         # O(n log n)
    return s              # O(1)  => загальна складність O(n^2log(n))


def e(n):
    prod = 1                   # O(1)
    for i in range(1, n+1):    # O(n)
        prod *= 1 / (1 + i)    # O(1)
    return prod                # O(1)  => загальна складність O(n)

def f(n):
    result = 1                     # O(1)
    for i in range(1, n+1):        # O(n)
        fact = 1                   # O(1)
        for j in range(1, i+1):    # O(n^2)
            fact *= j              # O(1)
        result *= 1 / (1 + fact)   # O(1)
    return result                  # O(1) => загальна складність O(n^2)

def g(n, a):
    result = 1                       # O(1)
    for i in range(1, n+1):          # O(n)
        fact = 1                     # O(1)
        for j in range(1, i+1):      # O(n^2)
            fact *= j                # O(1)
        result *= a**i / (1 + fact)  # O(1)
    return result                    # O(1)  => загальна складність O(n^2)

def h(n, m):
    res = 1                       # O(1)
    for i in range(1, n+1):       # O(n)
        res *= 1 / (1 + i**m)     # O(1)
    return res                    # O(1)  => загальна складність O(n)

def i(n):
    res = 1                     # O(1)
    for i in range(1, n+1):        # O(n)
        res *= 1 / (1 + i*i)    # O(1)
    return res                 # O(1)  => загальна складність O(n)




