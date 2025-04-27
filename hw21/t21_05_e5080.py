class Graph:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def count_lefs(self):
        amount = 0
        for line in self.matrix:
            if sum(line) == 1:
                amount += 1
        return amount


if __name__=="__main__":
    with open('input.txt') as f:
        n = int(f.readline())

        matrix = []
        for _ in range(n):
            line = list(map(lambda x: int(x), f.readline().split()))
            matrix.append(line)
            
        graph = Graph(matrix)
        print(graph.count_lefs())