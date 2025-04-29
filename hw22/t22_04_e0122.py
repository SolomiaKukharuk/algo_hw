class Graph:
    def __init__(self, adjacency_matrix, d):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)
        self.counter = 0
        self.visited = set()
        self.d = d

    def dfs(self, a, b, depth):
        if depth > d: return

        if a == b:
            self.counter += 1
            return
        
        self.visited.add(a)
        for i in range(self.n):
            if self.matrix[a][i] == 1 and i not in self.visited:
                self.dfs(i, b, depth+1)
        self.visited.remove(a)

    def get_result(self):
        return self.counter


if __name__=="__main__":
    with open('input.txt', 'r') as f:
        n, k, a, b, d = map(int, f.readline().split())

        matrix = [[0]*n for _ in range(n)]

        for _ in range(k):
            v, u = map(int, f.readline().split())
            matrix[v-1][u-1] = 1
        
        graph = Graph(matrix, d)
        graph.dfs(a-1, b-1, 0)
        print(graph.get_result())