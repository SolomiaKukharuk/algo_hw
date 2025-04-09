class Node:
    def __init__(self, key=None):
        self.node_key = key

    def is_empty(self):
        return self.node_key is None

    def set_key(self, key):
        self.node_key = key

    def get_key(self):
        return self.node_key


class Tree(Node):
    def __init__(self, key=None):
        super().__init__(key)
        self.children = []

    def is_empty(self):
        return super().is_empty() and len(self.children) == 0

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, key):
        for child in self.children:
            if child.get_key() == key:
                self.children.remove(child)
                return True
        return False

    def get_child(self, key):
        for child in self.children:
            if child.get_key() == key:
                return child
        return None

    def get_children(self):
        return self.children

    def count_colors(self):
        colors = set()
        for child in self.children:
            colors.update(child.count_colors())
        return colors.union({self.node_key})


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        num_nodes = int(file.readline())

        trees = [Tree(i + 1) for i in range(num_nodes)]

        for i in range(num_nodes):
            parent, color = map(int, file.readline().split())
            if parent != 0:
                trees[parent - 1].add_child(trees[i])
            trees[i].set_key(color)

        for tree in trees:
            print(len(tree.count_colors()), end=" ")
