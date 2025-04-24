from math import log2, gcd, ceil


class SegmentTree:
    def __init__(self, array) -> None:
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = [0] * n + array + [0] * (n-k)

        for i in range(n-1,0,-1):
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
        self.size = n
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        i = pos // 2
        while i > 1:
            self.items[i] = gcd(self.items[2*i], self.items[2*i+1])
            i = i // 2


    def gcd(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left%2==1:
                result = gcd(result, self.items[left])
            if right%2==0:
                result = gcd(result, self.items[right])
            left = (left+1)//2
            right= (right-1)//2
        return result


if __name__=="__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        array = list(map(lambda x: int(x), f.readline().split()))
        m = int(f.readline())

        tree = SegmentTree(array)
        for _ in range(m):
            q, l, r =  list(map(lambda x: int(x), f.readline().split()))
            if q == 1:
                print(tree.gcd(l-1, r-1))
            elif q == 2:
                tree.update(l-1, r)