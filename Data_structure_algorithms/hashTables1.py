class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def polynomial_hash(self, key, p=31):
        hash_value = 0
        p_pow = 1
        for char in key:
            hash_value = (hash_value + (ord(char) - ord("a") + 1) * p_pow) % self.size
            p_pow = (p_pow * p) % self.size
        return hash_value

    def insert(self, key, value):
        hash_index = self.polynomial_hash(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[hash_index].append([key, value])

    def search(self, key):
        hash_index = self.polynomial_hash(key)
        for pair in self.table[hash_index]:
            if pair[0] == key:
                return pair[1]

        return None


hash_table = HashTableChaining(10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
print(hash_table.search("apple"))  # Output: 1
print(hash_table.search("banana"))  # Output: 2
print(hash_table.search("cherry"))  # Output: None
