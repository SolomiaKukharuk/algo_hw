class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = node
        else:
            self._back.next = node
        self._back = node
        self._size += 1

    def pop(self):
        node = self._front
        self._front = self._front.next
        if self._size == 1:
            self._back = None
        self._size -= 1
        return node.item

    def size(self):
        return self._size


if __name__ == '__main__':
    with open('input.txt') as f:
        n = int(f.readline())
        first = list(map(int, f.readline().split()))
        second = list(map(int, f.readline().split()))

        first_queue = Queue()
        for el in first:
            first_queue.push(el)

        second_queue = Queue()
        for el in second:
            second_queue.push(el)

        counter = 0
        while first_queue.size() and second_queue.size():
            counter += 1
            if counter > 2E5:
                print('draw')
                break
            first_card = first_queue.pop()
            second_card = second_queue.pop()

            if (first_card == 0 and second_card == n - 1):
                first_queue.push(first_card)
                first_queue.push(second_card)
            elif (first_card == n - 1 and second_card == 0):
                second_queue.push(first_card)
                second_queue.push(second_card)
            else:
                if first_card > second_card:
                    first_queue.push(first_card)
                    first_queue.push(second_card)
                else:
                    second_queue.push(first_card)
                    second_queue.push(second_card)
        else:
            if first_queue.size():
                print(f'first {counter}')
            else:
                print(f'second {counter}')