class Graph:
    def __init__(self, matrix: list, vertex_amount: int) -> None:
        self.matrix = matrix
        self.vertex_amount = vertex_amount

    def check_multiedges(self):
        for line in matrix:
            if any( el>1 for el in line):
                print('YES')
                break
        else:
            print('NO')


if __name__=="__main__":
    with open('input.txt') as f:
        n, m = list(map(lambda x: int(x), f.readline().split()))

        matrix = [[0]*n for _ in range(n)]
        for _ in range(m):
            v1, v2 = list(map(lambda x: int(x), f.readline().split()))
            matrix[v1-1][v2-1]+=1

        graph = Graph(matrix, n)
        graph.check_multiedges()