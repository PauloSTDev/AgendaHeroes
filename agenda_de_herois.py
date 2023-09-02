class AgendaHeroes:
    def __init__(self, size = 25):
        self.size = size
        self.table = [None] * size
        self.total_items = 0
   
    def hash_function(self, key):
        print("index: {} - value: {}".format(ord(key[0])% self.size, key))
        ord_key = ord(key[0])
        hash = ord_key % self.size
        return hash


    def insert(self, key):
            if self.total_items == self.size:
                print("Full table")
                return False
            index = self.hash_function(key)
            if self.table[index] is None:
                self.table[index] = key
            else:
                while self.table[index] is not None:
                    index += 1
                    if index == self.size:
                        index = 0
                self.table[index] = key
            self.total_items += 1
            return True
   
    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return self.table[index]
            index += 1
            if index == self.size:
                index = 0
            if index == original_index:
                return None
        return None

heroes_hash = AgendaHeroes()

print(heroes_hash.table)
