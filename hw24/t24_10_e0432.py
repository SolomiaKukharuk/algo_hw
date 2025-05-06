from collections import deque

DIRECTIONS = [
    (0, 0, 1),  (0, 0, -1),
    (0, 1, 0),  (0, -1, 0),
    (1, 0, 0),  (-1, 0, 0)
]

def bfs(dungeon, L, R, C, start, end):
    visited = [[[False]*C for _ in range(R)] for _ in range(L)]
    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]][start[2]] = True

    while queue:
        l, r, c, minutes = queue.popleft()
        if (l, r, c) == end:
            return f'Escaped in {minutes} minute(s).'

        for dl, dr, dc in DIRECTIONS:
            nl, nr, nc = l + dl, r + dr, c + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if not visited[nl][nr][nc] and dungeon[nl][nr][nc] != '#':
                    visited[nl][nr][nc] = True
                    queue.append((nl, nr, nc, minutes + 1))
    return 'Trapped!'


def process():
    while True:
        LRC = input()
        if not LRC:
            continue
        L, R, C = map(int, LRC.split())
        if L == 0 and R == 0 and C == 0:
            break

        dungeon = []
        start = end = None

        for level in range(L):
            floor = []
            for _ in range(R):
                row = input()
                if 'S' in row:
                    start = (level, len(floor), row.index('S'))
                if 'E' in row:
                    end = (level, len(floor), row.index('E'))
                floor.append(list(row))
            dungeon.append(floor)
            input()

        print(bfs(dungeon, L, R, C, start, end))


if __name__ == "__main__":
    process()

