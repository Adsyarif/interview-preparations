class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_key].append([key, value])

    def search(self, key):
        hash_key = self._hash(key)
        for pair in self.table[hash_key]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        hash_key = self._hash(key)
        for i, pair in enumerate(self.table[hash_key]):
            if pair[0] == key:
                del self.table[hash_key][i]
                return

# Example usage:
hash_table = HashTable(10)
hash_table.insert('a', 1)
hash_table.insert('b', 2)
hash_table.insert('c', 3)

print(hash_table.search('b'))  # Output: 2

hash_table.delete('b')
print(hash_table.search('b'))  # Output: None
