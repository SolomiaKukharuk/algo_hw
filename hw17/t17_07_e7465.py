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
        elif key >= self.key:
            if self.right is None:
                self.right = SearchTree(key)
            else:
                self.right.insert(key)
    
    def has_left(self) -> bool:
        return self.left is not None
    def has_right(self) -> bool:
        return self.right is not None
    

def DFS(root, output: list):
    output.append(root.key)
    if root.has_left(): 
        DFS(root.left, output) 
    if root.has_right():
        DFS(root.right, output)

if __name__=='__main__':
    with open('input.txt') as f:
        n = f.readline()
        input1 = list(map(int, f.readline().split()))
        m = f.readline()
        input2 = list(map(int, f.readline().split()))

        # create first tree
        tree1 = SearchTree(input1[0])
        for elem in input1[1:]:
            tree1.insert(elem)

        # create second tree
        tree2 = SearchTree(input2[0])
        for elem in input2[1:]:
            tree2.insert(elem)
        
        output1 = list()
        DFS(tree1, output1)
        output2 = list()
        DFS(tree2, output2)

        if output1 == output2:
            print(1)
        else:
            print(0)
