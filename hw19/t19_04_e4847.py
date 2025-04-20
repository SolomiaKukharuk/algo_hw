class PQelement:
    def __init__(self, key=None, prior=None) -> None:
        self._key = key
        self._prior = prior
    
    def get_key(self):
        return self._key
    
    def upd_key(self, new_key):
        self._key = new_key
    
    def get_prior(self):
        return self._prior
    
    def upd_prior(self, new_prior):
        self._prior = new_prior


class PriorityQueue:
    """
    Бінарна купа з найбільшим вгорі
    """
    def __init__(self) -> None:
        self.items = []

    def ADD(self, id: str, priority: int):
        element = PQelement(id, priority)
        self.items.append(element)
        self.sift_up()
    
    def sift_up(self):
        i = len(self.items) - 1
        while i > 0:
            parent = (i-1) // 2
            if self.items[i].get_prior() > self.items[parent].get_prior():
                self.swap(parent, i)

            i = parent
    
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def POP(self):
        root = self.items[0]
        if len(self.items) > 1:
            self.swap(0, -1)
            self.items.pop()
            self.sift_down()
        else:
            self.items.pop()
        return root.get_key(), root.get_prior()
    
    def sift_down(self):
        i = 0
        while 2*i + 1 < len(self.items):
            left = 2*i + 1
            right = 2*i + 2
            max_child = left
            if right < len(self.items) and self.items[right] > self.items[left]:
                max_child = right
            if self.items[i].get_prior() < self.items[max_child].get_prior():
                self.swap(max_child, i)
            i = max_child

            
    def find_elem_index(self, id):
        i = 0
        for el in self.items:
            if el.get_key() == id:
                return i
            i += 1

    def CHANGE(self, id: str, new_priority: int):
        i = self.find_elem_index(id)
        old_prior =  self.items[i].get_prior()
        self.items[i].upd_prior(new_priority)

        if new_priority > old_prior:
            #sift up
            while i > 0:
                parent = (i-1) // 2
                if self.items[i].get_prior() > self.items[parent].get_prior():
                    self.swap(parent, i)
                else:
                    break
                i = parent
        else:
            #sift down
            while 2*i + 1 < len(self.items):
                left = 2*i + 1
                right = 2*i + 2
                max_child = left
                if right < len(self.items) and self.items[right] > self.items[left]:
                    max_child = right
                if self.items[i].get_prior() < self.items[max_child].get_prior():
                    self.swap(max_child, i)
                else:
                    break
                i = max_child   

    

if __name__=="__main__":
    with open("input.txt") as f:
        pq = PriorityQueue()
        for line in f:
            line = line.split()
            if line:
                if line[0] == 'ADD':
                    pq.ADD(line[1], int(line[2]))
                elif line[0] == 'CHANGE':
                    pq.CHANGE(line[1], int(line[2]))
                else:
                    print(*pq.POP())
