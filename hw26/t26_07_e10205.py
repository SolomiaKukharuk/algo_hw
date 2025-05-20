import sys
import math

input = sys.stdin.read
data = input().strip().split('\n')

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr != yr:
            self.p[yr] = xr
            return True
        return False

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def solve(n, coords, existing):
    dsu = DSU(n)
    for u, v in existing:
        dsu.union(u - 1, v - 1)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(coords[i], coords[j])
            edges.append((d, i, j))
    edges.sort()

    result = []
    for d, u, v in edges:
        if dsu.union(u, v):
            result.append((u + 1, v + 1))
    return result

i = 0
t = int(data[i].strip())
i += 1
results = []

for _ in range(t):
    while i < len(data) and data[i].strip() == "":
        i += 1
    n = int(data[i].strip())
    i += 1

    coords = []
    for _ in range(n):
        x, y = map(int, data[i].strip().split())
        coords.append((x, y))
        i += 1

    m = int(data[i].strip())
    i += 1

    existing = []
    for _ in range(m):
        u, v = map(int, data[i].strip().split())
        existing.append((u, v))
        i += 1

    res = solve(n, coords, existing)
    if res:
        results.append('\n'.join(f"{u} {v}" for u, v in res))
    else:
        results.append("No new highways need")

print('\n\n'.join(results))
