from math import log2,  ceil

class SegmentTree:
    def __init__(self, array) -> None:
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = [0] * n + array + [0] * (n-k)
        for i in range(n-1,0,-1):
            self.items[i] = self.items[2*i] + self.items[2*i+1]
        self.size = n
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        i = pos // 2
        while i > 1:
            self.items[i] = self.items[2*i] + self.items[2*i+1]
            i = i // 2


    def sum(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left%2==1:
                result += self.items[left]
            if right%2==0:
                result += self.items[right]
            left = (left+1)//2
            right= (right-1)//2
        return result
    
if __name__=="__main__":
    with open('input.txt') as f:
        n, q = list(map(lambda x: int(x), f.readline().split()))
        array = list(map(lambda x: int(x), f.readline().split()))

        tree = SegmentTree(array)


        for _ in range(q):
            line = f.readline().split()
            line = [line[0]] + list(map(lambda x: int(x), line[1:]))
            if line[0] == '?':
                l, r = line[1], line[2]
                print(tree.sum(l-1, r-1))
            else:
                i, j, d = line[1], line[2], line[3]
                for index in range(i, j+1):
                    tree.update(index-1,d)

                