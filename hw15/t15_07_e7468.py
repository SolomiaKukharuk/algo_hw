class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self._first = None
        self._last = None
        self._curr = None
        self._size = 0

    def empty(self) -> bool:
        return self._first is None

    def insert_after(self, item):
        node = Node(item)

        if self.empty():
            self._first = self._last = self._curr = node
        else:
            node.prev = self._curr
            if self._curr == self._last:
                self._last = node
            else:
                node.next = self._curr.next
                self._curr.next.prev = node

            self._curr.next = node
            self._curr = node

        self._size += 1

    def Print(self) -> None:
        output = str()
        curr = self._first
        while curr is not None:
            output = output + " " + str(curr.data)
            curr = curr.next
        print(output[1:])

    def ReorderList(self) -> None:
        curr = self._first
        for _ in range(self._size // 2):
            last = self._last
            self._last = last.prev

            last.next = curr.next
            curr.next.prev = last
            curr.next = last
            last.prev.next = None
            last.prev = curr
            curr = last.next


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        seq = f.readline().split()

        our_list = DoublyLinkedList()
        for el in seq:
            our_list.insert_after(el)

        our_list.ReorderList()
        our_list.Print()

