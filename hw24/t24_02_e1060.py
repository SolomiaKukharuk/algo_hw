from collections import deque

def solve_labyrinth(n, grid):
    start = goal = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                goal = (i, j)

    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    visited = [[False]*n for _ in range(n)]
    prev = [[None]*n for _ in range(n)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] in ('.', 'X'):
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)
                    queue.append((nx, ny))

    if not visited[goal[0]][goal[1]]:
        print("N")
        return

    x, y = goal
    while (x, y) != start:
        grid[x][y] = '+'
        x, y = prev[x][y]

    print("Y")
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    solve_labyrinth(n, grid)
