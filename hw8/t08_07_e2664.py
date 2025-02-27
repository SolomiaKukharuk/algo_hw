def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        sorted = True
        curr_el = arr[i]
        index = i
        while index > 0:
            if arr[index - 1] > curr_el:
                arr[index] = arr[index - 1]
                sorted = False
            else:
                break
            index -= 1
        arr[index] = curr_el
        if not sorted: print(*arr)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        insertion_sort(array)
