class Node:
    def __init__(self, item=None) -> None:
        self.item = item
        self.prev = None
        self.next = None


class Deque:
    def __init__(self) -> None:
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, n) -> str:
        node = Node(n)
        node.next = self._front
        if self.size() != 0:
            self._front.prev = node
        else:
            self._back = node
        self._front = node

        self._size += 1
        return 'ok'

    def push_back(self, n) -> str:
        node = Node(n)
        node.prev = self._back
        if self.size() != 0:
            self._back.next = node
        else:
            self._front = node
        self._back = node

        self._size += 1
        return 'ok'

    def pop_front(self) -> int:
        if self.size() != 0:
            result = self._front.item
            self._front = self._front.next
            if self._front is None:
                self._back = None
            else:
                self._front.prev = None

            self._size -= 1
            return result
        else:
            return 'error'

    def pop_back(self) -> int:
        if self.size() != 0:
            result = self._back.item
            self._back = self._back.prev
            if self._back is None:
                self._front = None
            else:
                self._back.next = None

            self._size -= 1
            return result
        else:
            return 'error'

    def front(self) -> int:
        if self.size() != 0:
            return self._front.item
        else:
            return 'error'

    def back(self) -> int:
        if self.size() != 0:
            return self._back.item
        else:
            return 'error'

    def size(self) -> int:
        return self._size

    def clear(self) -> str:
        self._front = None
        self._back = None
        self._size = 0
        return 'ok'

    @staticmethod
    def exit() -> str:
        return 'bye'

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    deque = Deque()
    with open('input.txt') as f:
        for line in f:
            result = deque.execute(line)
            print(result)
            if result == 'bye': break