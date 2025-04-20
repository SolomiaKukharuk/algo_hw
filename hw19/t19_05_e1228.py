class Heap:
    def __init__(self) -> None:
        self.items = [0]
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.sift_up()

    def sift_up(self):
        i = len(self.items) - 1
        while i > 1:
            parent = i // 2
            if self.items[i] < self.items[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent
    
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
    
    def extract_minimum(self):
        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.size -= 1
        self.sift_down()
        return root
    
    def sift_down(self):
        i = 1
        while 2*i <= self.size:
            left = 2*i
            right = 2*i+1
            min_child = self.min_child(left, right)
            if self.items[i]>self.items[min_child]:
                self.swap(min_child, i)
            else:
                break
            i = min_child
    
    def min_child(self, left, right):
        if right > self.size:
            return left
        else:
            if self.items[left] < self.items[right]:
                return left
            else:
                return right


if __name__=="__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        numbers = list(map(lambda x: int(x), f.readline().split()))

        heap = Heap()
        for number in numbers:
            heap.insert(number)

        result = 0
        while heap.get_size()>1:
            n1 = heap.extract_minimum()
            n2 = heap.extract_minimum()
            value = n1 + n2
            result += value
            heap.insert(value)
        else:
            print(result)