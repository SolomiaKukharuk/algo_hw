
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

M = 10000019
N = 31

def _hash(S: str) -> int:
    h = 0
    for i in range(len(S)):
        h = h * N + ord(S[i])
    return h % M


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global books
    books = [None for _ in range(M)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    curr = _hash(author)
    node = books[curr]
    while node is not None:
        if node.key == author and node.value == title:
            node.key = author
            node.value = title
            return
        node = node.next

    node = Node(author, title)
    node.next = books[curr]
    books[curr] = node


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    curr = _hash(author)
    node = books[curr]
    while node is not None:
        if node.key == author and node.value == title:
            return True
        node = node.next
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    curr = _hash(author)
    node = books[curr]
    if node is not None:
        if node.key == author and node.value == title:
            books[curr] = node.next
            return

        prev = node
        node = node.next
        while node is not None:
            if node.key == author and node.value == title:
                prev.next = node.next
                return

            prev = node
            node = node.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    curr = _hash(author)
    node = books[curr]
    res = []
    while node is not None:
        res.append(node.value)
        node = node.next
    return sorted(res)

