def butterflies(arr, t):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == t:
            return True
        elif arr[m] < t:
            l = m + 1
        else:
            r = m - 1
    return False


if __name__ == "__main__":
    try:
        n = int(input().strip())
        arr1 = list(map(int, input().split()))
        if len(arr1) != n:
            raise ValueError("Некоректна кількість елементів у масиві колекції")
        m = int(input().strip())
        arr2 = list(map(int, input().split()))
        if len(arr2) != m:
            raise ValueError("Некоректна кількість елементів у масиві запитів")
        for query in arr2:
            print("YES" if butterflies(arr1, query) else "NO")

    except (ValueError, IndexError):
        print("Помилка у вхідних даних")