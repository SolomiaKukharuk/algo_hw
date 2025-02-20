class HashTable:
    def __init__(self, size=13):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def put(self, key):
        index = self.hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def unique_count(self):
        return sum(len(bucket) for bucket in self.table)

if __name__ == "__main__":
    phone_numbers = []
    try:
        n = int(input().strip())
        phone_numbers = input().strip().split()
        phone_book = HashTable()
        for number in phone_numbers:
            phone_book.put(number)
        unique_contacts = phone_book.unique_count()
        print(unique_contacts)


    except EOFError:
        pass

