class SearchTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = SearchTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)
    
    def search(self, key):
        result = list()
        node = self
        result.append(node.key)
        while node is not None:
            if node.key == key:
                return result
            elif node.key > key:
                node = node.left 
            else:
                node = node.right
            result.append(node.key)
        return None

if __name__=='__main__':
    with open('input.txt') as f:
        input = " "
        for line in f:
            input += f" {line}"
        input = list(map(int, line.split()))
        tree = SearchTree(input[0])

        for elem in input[1:]:
            tree.insert(elem)
        
        result = tree.search(input[-1])
        if result == input:
            print('YES')
        else:
            print('NO')