class Graph:
    def __init__(self, vertex_amount: int) -> None:
        self.adjacency_list = {v: [] for v in range(1, vertex_amount + 1)}
    

    def add_edge(self, v1, v2) -> None:
        # неорієнтований граф
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)


    def check_complete_graph(self):
        our_list = self.adjacency_list
        our_list_len = len(our_list)
        if all(len(set(our_list[el]))==our_list_len-1 for el in our_list):
            print('YES')
        else:
            print('NO')


if __name__=="__main__":
    with open('input.txt') as f:
        n, m = list(map(lambda x: int(x), f.readline().split()))

        graph = Graph(n)
        for _ in range(m):
            v1, v2 = list(map(lambda x: int(x), f.readline().split()))
            graph.add_edge(v1, v2)
        
        graph.check_complete_graph()
