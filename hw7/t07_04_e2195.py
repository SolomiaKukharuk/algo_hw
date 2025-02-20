import math
import string

EMPTY = None


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class HashTable:

    M = 31

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]
        self._values: list[EMPTY | list[str]] = [EMPTY for _ in range(size)]

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values
        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i], _values[i])

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self._size

    def get(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size

    def set(self, key: str, value):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key
        self._values[i] = value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return False if self.get(key) is None else True

class VocabularyChecker:
    def __init__(self, n, m, vocabulary_words, text_lines):
        self.n = n
        self.m = m
        self.vocabulary_words = vocabulary_words
        self.text_lines = text_lines
        self.vocabulary = HashTable()
        self.text_hash = HashTable()

    def process_text(self):
        """Обробляє текст: видаляє розділові знаки та переводить у нижній регістр."""
        words = []
        word = ""
        for line in self.text_lines:
            for char in line:
                if char.isalpha():
                    word += char.lower()
                else:
                    if word:
                        words.append(word)
                        word = ""
            if word:
                words.append(word)
                word = ""
        return words

    def build_vocabulary(self):
        """Додає слова словника у хеш-таблицю."""
        for word in self.vocabulary_words:
            self.vocabulary.set(word.lower(), True)

    def build_text_hash(self, text_words):
        """Додає слова з тексту у хеш-таблицю."""
        for word in text_words:
            self.text_hash.set(word, True)

    def check_text_with_vocabulary(self):
        """Перевіряє виконання умов задачі."""
        self.build_vocabulary()
        text_words = self.process_text()
        self.build_text_hash(text_words)

        # Перевірка: якщо слово з тексту відсутнє у словнику
        for word in text_words:
            if word not in self.vocabulary:
                return "Some words from the text are unknown."

        # Перевірка: якщо слово словника не зустрічається у тексті
        for word in self.vocabulary_words:
            if word.lower() not in self.text_hash:
                return "The usage of the vocabulary is not perfect."

        return "Everything is going to be OK."


import math
import string
import sys

EMPTY = None

def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

class HashTable:

    M = 31

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys = [EMPTY for _ in range(size)]
        self._values = [EMPTY for _ in range(size)]

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _keys = self._keys
        _values = self._values
        self.__init__(self._size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i], _values[i])

    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = h * self.M + ord(s[i])
        return h % self._size

    def get(self, key: str):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]
            i = (i + 1) % self._size
        return None

    def set(self, key: str, value):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value
                return
            i = (i + 1) % self._size

        self._count += 1
        self._keys[i] = key
        self._values[i] = value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return False if self.get(key) is None else True


class VocabularyChecker:
    def __init__(self, n, m, vocabulary_words, text_lines):
        self.n = n
        self.m = m
        self.vocabulary_words = vocabulary_words
        self.text_lines = text_lines
        self.vocabulary = HashTable()
        self.text_hash = HashTable()

    def process_text(self):

        words = []
        word = ""
        for line in self.text_lines:
            for char in line:
                if char.isalpha():
                    word += char.lower()
                else:
                    if word:
                        words.append(word)
                        word = ""
            if word:
                words.append(word)
                word = ""
        return words

    def build_vocabulary(self):

        for word in self.vocabulary_words:
            self.vocabulary.set(word.lower(), True)

    def build_text_hash(self, text_words):

        for word in text_words:
            self.text_hash.set(word, True)

    def check_text_with_vocabulary(self):

        self.build_vocabulary()
        text_words = self.process_text()
        self.build_text_hash(text_words)


        for word in text_words:
            if word not in self.vocabulary:
                return "Some words from the text are unknown."

        for word in self.vocabulary_words:
            if word.lower() not in self.text_hash:
                return "The usage of the vocabulary is not perfect."

        return "Everything is going to be OK."



if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split('\n')
    n, m = map(int, input_data[0].split())
    vocabulary_words = [line.strip() for line in input_data[1:1 + n]]
    text_lines = input_data[1 + n:1 + n + m]

    checker = VocabularyChecker(n, m, vocabulary_words, text_lines)
    result = checker.check_text_with_vocabulary()

    print(result)



