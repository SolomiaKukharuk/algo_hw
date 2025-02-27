def bubble_sort_counter(arr: list) -> int:
    n = len(arr)
    counter = 0
    for i in range(n -1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                counter += 1
    return counter



if __name__=="__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        array = list(map(int, f.readline().split()))
        print(bubble_sort_counter(array))