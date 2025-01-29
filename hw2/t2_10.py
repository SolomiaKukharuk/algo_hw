def f(n):
    sum = 0                       #O(1)
    for i in range(1,n + 1):      #O(n)
        sum += i                  #O(n)
    return sum                    #O(n)

#res: O(n)
#sum{i = 1; n}i = n * (n + 1) // 2
# Покращена функція де оцінка буде O(1):
def F(n):
    return n * (n + 1) // 2
