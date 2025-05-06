class Graph:

    def __init__(self, adjacency_matrix):
        self.matrix = adjacency_matrix
        self.n = len(adjacency_matrix)
        self.results = []

    def components_count(self):
        remaining = set(range(self.n))
        stack = []
        count = 0
        result = []
        while remaining or stack:
            if stack:
                i = stack.pop()
                result.append(i+1)
            else:
                self.results.append(result)
                result = []
                i = remaining.pop()
                result.append(i+1)
                count += 1

            for j in range(self.n):
                if self.matrix[i][j] == 1 and j in remaining:
                    stack.append(j)
                    remaining.remove(j)
        else:
            self.results.append(result)
            
        return count
    
    def print_result(self):
        for result in self.results[1:]:
            print(len(result))
            print(*result)


if __name__=='__main__':
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        
        matrix = [[0]*n for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            matrix[u-1][v-1] = 1
            matrix[v-1][u-1] = 1

        
        graph = Graph(matrix)
        print(graph.components_count())
        graph.print_result()