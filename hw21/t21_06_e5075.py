class Graph:
    def __init__(self, matrix: list, vertex_amount: int) -> None:
        self.matrix = matrix
        self.vertex_amount = vertex_amount

    def vertex_degrees(self):
        for i in range(self.vertex_amount):
            # напівтепені виходу
            deg_out = sum(matrix[i])    

            # напівтепені входу
            deg_in = 0
            for j in range(self.vertex_amount):
                deg_in += matrix[j][i]

            print(deg_in, deg_out)


if __name__=="__main__":
    with open('input.txt') as f:
        n, m = list(map(lambda x: int(x), f.readline().split()))

        matrix = [[0]*n for _ in range(n)]
        for _ in range(m):
            v1, v2 = list(map(lambda x: int(x), f.readline().split()))
            matrix[v1-1][v2-1]=1

        graph = Graph(matrix, n)
        graph.vertex_degrees()