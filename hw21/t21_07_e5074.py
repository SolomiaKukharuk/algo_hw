class Graph:
    def __init__(self, matrix: list, vertex_amount: int) -> None:
        self.matrix = matrix
        self.vertex_amount = vertex_amount

    def vertex_degrees(self):
        """
        головна ідея: 
        сума в і-му рядку - степінь і+1 вершини
        """
        for i in range(self.vertex_amount):
            deg = sum(matrix[i])    
            print(deg)


if __name__=="__main__":
    with open('input.txt') as f:
        n, m = list(map(lambda x: int(x), f.readline().split()))

        matrix = [[0]*n for _ in range(n)]
        for _ in range(m):
            v1, v2 = list(map(lambda x: int(x), f.readline().split()))
            matrix[v1-1][v2-1]=1
            matrix[v2-1][v1-1]=1

        graph = Graph(matrix, n)
        graph.vertex_degrees()