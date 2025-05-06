class Graph:

    def __init__(self, size):
        self.vertices = {v: [] for v in range(1, size + 1)}

    def add_edge(self, u, v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)

    def is_connected(self):
        remaining = set(self.vertices)
        stack = [remaining.pop()]
        while stack:
            vertex = stack.pop()
            for neighbour in self.vertices[vertex]:
                if neighbour in remaining:
                    stack.append(neighbour)
                    remaining.remove(neighbour)
        return len(remaining) == 0

if __name__=='__main__':
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        edges = list()
        for _ in range(m):
            edge = f.readline().split()
            edges.append(edge)

        # print(edges)
        k = int(f.readline())
        edges_copy = edges[:]
        for _ in range(k):
            line = list(map(int, f.readline().split()[1:]))
            for edge in line:
                edges[edge-1] = None

            graph = Graph(n)
            for edge in edges:
                if edge is not None:
                    a, b = map(int, edge)
                    graph.add_edge(a, b)

            if graph.is_connected():
                print('Connected')
            else:
                print('Disconnected')
            edges = edges_copy[:]
            