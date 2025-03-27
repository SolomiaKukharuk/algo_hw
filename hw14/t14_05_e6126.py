class Queue:
    def __init__(self) -> None:
        self._items = list()

    def push(self, n) -> str:
        self._items.append(n)
        return 'ok'

    def pop(self) -> int:
        if self.size() != 0:
            return self._items.pop(0)
        else:
            return 'error'

    def front(self) -> int:
        if self.size() != 0:
            return self._items[0]
        else:
            return 'error'

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> str:
        self._items.clear()
        return 'ok'

    @staticmethod
    def exit() -> str:
        return 'bye'

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    queue = Queue()
    with open('input.txt') as f:
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == 'bye': break