from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)

    def depth_first_search(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self.depth_first_search(neighbor, visited, stack)
        stack.append(vertex)

    def get_transpose(self):
        transpose_graph = Graph(self.num_vertices)
        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                transpose_graph.add_edge(neighbor, vertex)
        return transpose_graph

    def count_components(self):
        stack = []
        visited = [False] * self.num_vertices
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self.depth_first_search(vertex, visited, stack)

        transpose_graph = self.get_transpose()
        visited = [False] * self.num_vertices
        count = 0
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                transpose_graph.depth_first_search(vertex, visited, [])
                count += 1
        return count


if __name__=='__main__':
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u-1,v-1)

        num_components = graph.count_components()
        print(num_components)