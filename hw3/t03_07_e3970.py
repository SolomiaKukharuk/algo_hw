def binary_search_left(array, x):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_right(array, x):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left

def count_occurrences(array, queries):
    if not array:
        return [0] * len(queries)

    results = []
    for x in queries:
        left = binary_search_left(array, x)
        right = binary_search_right(array, x)
        results.append(right - left)

    return results

if __name__ == "__main__":
    try:
        n = int(input().strip())
        array = list(map(int, input().split())) if n > 0 else []
        m = int(input().strip())
        queries = list(map(int, input().split())) if m > 0 else []
        if n == 0:
            print("\n".join(["0"] * m))
        results = count_occurrences(array, queries)
        print("\n".join(map(str, results)))

    except (ValueError, EOFError):
        pass

