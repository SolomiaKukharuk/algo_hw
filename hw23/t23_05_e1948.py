class Graph:
    def __init__(self, n):
        self.vertices = {
            v: [] for v in range(0, n)
        }
        self.size = n

    def add_edge(self, u, v):
        self.vertices[u].append(v)


def topological_sort(graph):
    incoming_counts = {node: 0 for node in graph.vertices}
    for node in graph.vertices:
        for neighbor in graph.vertices[node]:
            incoming_counts[neighbor] += 1
    
    no_incoming_nodes = []
    for node in graph.vertices:
        if incoming_counts[node] == 0:
            no_incoming_nodes.append(node)
    
    sorted_order = []
    while len(no_incoming_nodes) > 0:
        current_node = no_incoming_nodes.pop()
        sorted_order.append(current_node+1)

        for neighbor in graph.vertices[current_node]:
            incoming_counts[neighbor] -= 1
            if incoming_counts[neighbor] == 0:
                no_incoming_nodes.append(neighbor)
    
    if len(sorted_order) == len(graph.vertices):
        return sorted_order
    else:
        return [-1]



if __name__=='__main__':
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        
        graph = Graph(n)
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph.add_edge(u-1, v-1)

        print(*topological_sort(graph))