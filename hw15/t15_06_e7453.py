class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddToTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def RotateRight(self, k):
        if not self.head or not self.head.next or k == 0:
            return

        
        length = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = self.head

        k %= length
        if k == 0:
            curr.next = None
            return

        steps_to_new_tail = length - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        self.tail = new_tail
        self.tail.next = None

    def Print(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def copy(self):
        new_list = List()
        curr = self.head
        while curr:
            new_list.AddToTail(curr.data)
            curr = curr.next
        return new_list


if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    lst = List()
    for val in values:
        lst.AddToTail(val)

    try:
        while True:
            line = input()
            if not line.strip():
                break
            k = int(line)
            lst.RotateRight(k)
            lst.Print()
    except EOFError:
        pass

