def minimum_bribe(data):
    import sys
    sys.setrecursionlimit(10000)

    N = data[0]
    bribes = [0] * (N + 1)
    tree = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        entry = data[i]
        bribes[i] = entry[0]
        k = entry[1]
        if k > 0:
            for j in range(k):
                tree[i].append(entry[2 + j])

    def dfs(node):
        if not tree[node]:
            return bribes[node]
        min_subordinate = float('inf')
        for child in tree[node]:
            val = dfs(child)
            if val < min_subordinate:
                min_subordinate = val
        return bribes[node] + min_subordinate

    return dfs(1)


if __name__ == "__main__":
    import sys
    input_lines = sys.stdin.read().splitlines()
    N = int(input_lines[0])
    data = [N]
    for i in range(1, N + 1):
        row = list(map(int, input_lines[i].split()))
        data.append(row)
    print(minimum_bribe(data))
