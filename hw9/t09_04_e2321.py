def qsort(array, a, b):
    if a >= b:
        return
    pivot = array[a+(b-a)//2]
    left = a
    right = b

    while True:
        while array[left]<pivot:
            left += 1
        while array[right]>pivot:
            right -= 1
        if left>=right: break

        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    qsort(array, a, right)
    qsort(array, right+1, b)


if __name__=="__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        qsort(array, 0, len(array)-1)
        print(*array)