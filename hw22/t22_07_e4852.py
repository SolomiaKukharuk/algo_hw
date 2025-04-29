from collections import deque

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def get_distances(self, start):
        queue = deque([start])
        visited = set([start])
        distances = [-1]*self.n
        distances[start]=0
        while queue:
            u = queue.popleft()
            for v in range(self.n):
                if self.matrix[u][v] == 1 and v not in visited:
                    distances[v] = distances[u] + 1
                    visited.add(v)
                    queue.append(v)
        return distances
    
    
if __name__=="__main__":
    with open('input.txt', 'r') as f:
        n, a = map(int, f.readline().split())
        matrix = []
        for _ in range(n):
            line = list(map(int, f.readline().split()))
            matrix.append(line)
        graph = Graph(matrix)
        print(*graph.get_distances(a-1))
