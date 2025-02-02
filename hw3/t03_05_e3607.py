def height(arr, m, x):
    count = 0
    for el in arr:
        if m <= el <= x:
            count += 1
    return count


arr = []
while True:
    try:
        data = input().split()
        if not data:
            break
        if len(data) == 1:
            n = int(data[0])
        elif len(data) > 2:
            arr = list(map(int, data))
        else:
            m, x = map(int, data)
            print(height(arr, m, x))
    except EOFError:
        break
