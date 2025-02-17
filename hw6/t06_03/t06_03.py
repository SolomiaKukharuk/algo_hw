
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

M = 10000019
N = 137

def _hash(S: str) -> int:
    h = 0
    for i in range(len(S)):
        h = h * N + ord(S[i])
    return h % M


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global authors, titles
    authors = [None for _ in range(M)]
    titles = [None for _ in range(M)]


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    curr = _hash(author)
    while authors[curr] is not None and authors != "deleted":
        if authors[curr] == author and titles[curr] == title:
            return
        curr = (curr+1)%M
    authors[curr]=author
    titles[curr]=title


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    curr = _hash(author)
    while authors[curr] is not None and authors != "deleted":
        if authors[curr] == author and titles[curr] == title:
            return True
        curr = (curr+1)%M
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    curr = _hash(author)
    while find(author, title):
        if authors[curr]==author and titles[curr] == title:
            authors[curr]="deleted"
            titles[curr]="deleted"
        curr = (curr+1)%M



def findByAuthor(author: str) -> list:
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    curr = _hash(author)
    res = []
    while authors[curr] is not None and authors != "deleted":
        if authors[curr] == author :
            res.append((titles[curr]))
        curr = (curr + 1) % M
    return sorted(res)
