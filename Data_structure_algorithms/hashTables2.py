class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def polynomial_hash(self, key, p=31):
        hash_value = 0
        p_pow = 1
        for char in key:
            hash_value = (hash_value + (ord(char) - ord("a") + 1) * p_pow) % self.size
            p_pow = (p_pow * p) % self.size
        return hash_value

    def insert(self, key, value):
        index = self.polynomial_hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        self.table[index] = (key, value)

    def search(self, key):
        index = self.polynomial_hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None

    def delete(self, key):
        index = self.polynomial_hash(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == original_index:
                break


hash_table = HashTableLinearProbing(10)

# 데이터 삽입
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("grape", 3)

# 데이터 검색
print(hash_table.search("apple"))   # Output: 1
print(hash_table.search("banana"))  # Output: 2
print(hash_table.search("grape"))   # Output: 3
print(hash_table.search("cherry"))  # Output: None

# 데이터 삭제
hash_table.delete("banana")

# 삭제 후 데이터 검색
print(hash_table.search("banana"))  # Output: None
