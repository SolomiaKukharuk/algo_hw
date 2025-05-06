import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    stack = [(r, c)]
    visited[r][c] = True
    size = 1

    while stack:
        y, x = stack.pop()
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if grid[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    size += 1
                    stack.append((ny, nx))
    return size



N, M, K = map(int, input().split())
grid = [[False]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    grid[r-1][c-1] = True


max_lake = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] and not visited[i][j]:
            max_lake = max(max_lake, dfs(i, j))

print(max_lake)
