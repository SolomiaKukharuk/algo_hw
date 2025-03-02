def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        lefthalf = array[:m]
        righthalf = array[m:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] <= righthalf[j][0]:  # main feature
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        robot_list = list()
        for line in f:
            robot = tuple(map(int, line.split()))
            robot_list.append(robot)
        merge_sort(robot_list)
        for robot in robot_list:
            print(*robot)
