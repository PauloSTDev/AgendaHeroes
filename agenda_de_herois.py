import string
import csv

class AgendaHeroes:
    def __init__(self, size = 26):
        self.size = size
        self.table = [None] * size
        self.total_items = 0
        self.alphabet = list(string.ascii_lowercase)
   
    def hash_function(self, key, value = ''):
        key = key.lower()
        hash = ord(key[0]) - 97
        print("index: {} - value: {}".format(hash, key))
        return hash


    def insert(self, key):
            if self.total_items == self.size:
                print("Full table")
                return False

            index = self.hash_function(key)

            if index >= self.size:
                return print("Invalid Name")

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

arquivo = open("agenda.csv", "r")
reader = csv.reader(arquivo)
for linha in reader:
    heroes_hash.insert(linha[0])
    if linha[0] == "Sophia Carter":
        break

print(heroes_hash.table)