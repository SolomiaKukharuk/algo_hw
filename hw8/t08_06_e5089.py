def selection_sort(arr: list):
    n = len(arr)
    for i in range(n-1,0,-1):
        max_el_index = 0
        for j in range(1, i+1):
            if arr[max_el_index] < arr[j]:
                max_el_index = j
        arr[max_el_index], arr[i] = arr[i], arr[max_el_index]


if __name__=="__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        dictionary = []
        for line in f:
            dictionary.append(line[:-1])
        selection_sort(dictionary)
        for word in dictionary:
            print(word)