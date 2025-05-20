import sys
input = sys.stdin.read

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            self.parent[yr] = xr
            return True
        return False

def solve():
    data = input().split()
    idx = 0
    n, m, p = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    insecure = set(int(data[idx + i]) - 1 for i in range(p))
    idx += p

    edges_safe = []   
    edges_connect = []

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        w = int(data[idx+2])
        idx += 3

        if u in insecure and v in insecure:
            continue
        elif u in insecure or v in insecure:
            edges_connect.append((w, u, v))
        else:
            edges_safe.append((w, u, v))

    dsu = DSU(n)
    total_cost = 0
    components = n

    edges_safe.sort()
    for w, u, v in edges_safe:
        if dsu.union(u, v):
            total_cost += w
            components -= 1

    edges_connect.sort()
    used_insecure = set()
    for w, u, v in edges_connect:
        insecure_node = u if u in insecure else v
        if insecure_node in used_insecure:
            continue

        if dsu.union(u, v):
            total_cost += w
            components -= 1
            used_insecure.add(insecure_node)

    if components == 1:
        print(total_cost)
    else:
        print("impossible")

solve()