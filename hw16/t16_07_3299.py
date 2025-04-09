from sys import stdin, setrecursionlimit
setrecursionlimit(1_000_000)

def compute_lca_sum(n, m, parent_list, a1, a2, x, y, z):

    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent_list[i - 1]].append(i)

    LOG = 17
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(v, p):
        up[v][0] = p
        for i in range(1, LOG):
            if up[v][i - 1] != -1:
                up[v][i] = up[up[v][i - 1]][i - 1]
        for u in tree[v]:
            if u != p:
                depth[u] = depth[v] + 1
                dfs(u, v)

    dfs(0, -1)

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in reversed(range(LOG)):
            if depth[u] - (1 << i) >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    a = [a1, a2]
    ans = lca(a[0], a[1])
    total = ans

    for i in range(2, 2 * m, 2):
        a1_new = (x * a[i - 2] + y * a[i - 1] + z) % n
        a2_new = (x * a[i - 1] + y * a1_new + z) % n
        a.append(a1_new)
        a.append(a2_new)
        u = (a1_new + ans) % n
        v = a2_new
        ans = lca(u, v)
        total += ans

    return total


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    raw = input().split()

    if not raw:
        n, m = 3, 2
        parent_list = [0, 1]
        a1, a2 = 2, 1
        x, y, z = 1, 1, 0
    else:
        data = list(map(int, raw))
        ptr = 0
        n = data[ptr]
        m = data[ptr + 1]
        ptr += 2

        parent_list = data[ptr:ptr + n - 1]
        ptr += n - 1

        a1 = data[ptr]
        a2 = data[ptr + 1]
        ptr += 2

        x = data[ptr]
        y = data[ptr + 1]
        z = data[ptr + 2]

    result = compute_lca_sum(n, m, parent_list, a1, a2, x, y, z)
    print(result)
