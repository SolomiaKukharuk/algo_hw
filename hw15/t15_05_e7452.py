class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class List:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def empty(self) -> bool:
        return self._head is None

    def addToTail(self, val: int) -> None:

        node = Node(val)

        if self.empty():
            self._head = node
        elif self._tail is None:
            self._head.next = node
            self._tail = node
        else:
            curr = self._tail
            while True:
                if curr.next is None:
                    curr.next = node
                    break
                curr = curr.next

    def Print(self) -> None:
        output = str(self._head.data)
        curr = self._tail
        while curr is not None:
            output = output + " " + str(curr.data)
            curr = curr.next
        print(output)

    def PrintReverse(self) -> None:
        output = str(self._head.data)
        curr = self._tail
        while curr is not None:
            output = str(curr.data) + " " + output
            curr = curr.next
        print(output)


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        seq = f.readline().split()

        our_list = List()
        for el in seq:
            our_list.addToTail(el)

        our_list.Print()
        our_list.PrintReverse()