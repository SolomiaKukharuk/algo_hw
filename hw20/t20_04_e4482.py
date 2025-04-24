from math import log2, gcd, lcm, ceil


class SegmentTree_gcd:
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

    def get_gcd(self, left, right):
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
    


class SegmentTree_lcm:
    def __init__(self, array) -> None:
        k = len(array)
        n = 1 << ceil(log2(k))
        self.items = [1] * n + array + [1] * (n-k)

        for i in range(n-1,0,-1):
            self.items[i] = lcm(self.items[2*i], self.items[2*i+1])
        self.size = n
    
    def update(self, pos, x):
        pos += self.size
        self.items[pos] = x
        i = pos // 2
        while i > 1:
            self.items[i] = lcm(self.items[2*i], self.items[2*i+1])
            i = i // 2
    
    def get_lcm(self, left, right):
        left += self.size
        right += self.size
        result = 1
        while left <= right:
            if left%2==1:
                result = lcm(result, self.items[left])
            if right%2==0:
                result = lcm(result, self.items[right])
            left = (left+1)//2
            right= (right-1)//2
        return result
    

if __name__=="__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        array = list(map(lambda x: int(x), f.readline().split()))
        m = int(f.readline())

        tree_gcd = SegmentTree_gcd(array)
        tree_lcm = SegmentTree_lcm(array)
        for _ in range(m):
            q, l, r =  list(map(lambda x: int(x), f.readline().split()))
            if q == 1:
                gcd_temp = tree_gcd.get_gcd(l-1, r-1)
                lcm_temp = tree_lcm.get_lcm(l-1, r-1)
                if gcd_temp < lcm_temp :
                    print('wins') 
                elif gcd_temp > lcm_temp:
                    print('loser')
                else:
                    print('draw')
            elif q == 2:
                tree_gcd.update(l-1, r)
                tree_lcm.update(l-1, r)