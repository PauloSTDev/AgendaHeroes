import string
import csv

class AgendaHeroes:
    def __init__(self, size = 26):
        self.size = size
        self.total_items = 0
        self.hash_table = [(string.ascii_lowercase), [None] * size, [None] * size]
   
    def hash_function(self, key):
        original_name = key
        key = key.lower()
        hash = ord(key[0]) - 97
        print("index: {}:{} - value: {}".format(self.hash_table[0][hash].upper(),hash, original_name))
        return hash

    def insert(self, key, value):
            if self.total_items == self.size:
                print("Full table")
                return False
            index = self.hash_function(key)
            if index >= self.size or index < 0:
                return print("Invalid Name")
            if self.hash_table[1][index] is None:
                self.hash_table[1][index] = key
                self.hash_table[2][index] = value
                return print("Add completed!")
            else:
                while self.hash_table[1][index] is not None:
                    index += 1
                    if index == self.size:
                        index = 0
                self.hash_table[1][index] = key
                self.hash_table[2][index] = value
                print("Add completed!")
            self.total_items += 1   
            return True
   
    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.hash_table[1][index] is not None:
            if self.hash_table[1][index] == key:
                print("{}, {}".format(self.hash_table[1][index], self.hash_table[2][index]))
            if self.hash_table[1][index + 1] == None:
                return True
            index += 1
            if index == self.size:
                index = 0
            if index == original_index:
                return "Not in List"
        return "Not in list"
    
    def searchByWord(self, key):
        index = self.hash_function(key)
        original_index = index
        counter = 0
        while counter < self.size:
            if self.hash_table[1][index] != None and self.hash_table[1][index].lower().startswith(key.lower()):
                print("{}".format(self.hash_table[1][index]))
            index += 1
            counter += 1
            if index == self.size:
                index = 0
        return "Not in list"

    def delete(self, key):
        index = self.hash_function(key)
        if index >= self.size or index < 0:
            return print("Invalid Name")
        if (self.hash_table[1][index] == key):
            self.hash_table[1][index] = None
            self.hash_table[2][index] = None
            self.total_items -= 1
            return print("Delete completed!")
        else:
            while self.hash_table[1][index] is not None:
                    index += 1
                    if index == self.size:
                        index = 0
                    if (self.hash_table[1][index] == key):
                        self.hash_table[1][index] = None
                        self.hash_table[2][index] = None
                        print("Delete completed!")
                        self.total_items -= 1
                        return True
            
        return print("Not found")
    
    def add_contacts_from_diary(self):
        # Abertura e leitura de arquivo de agenda
        arquivo = open("agenda.csv", "r")
        reader = csv.reader(arquivo)

        # Adiciona contatos até a Abigail
        for linha in reader:
            self.insert(linha[0], linha[1])
            if linha[0] == "Abigail Quinn":
                break

    def showNames(self):
        for name in self.hash_table[1]:
            if (name != None):
                print(name)

    def showNumbers(self):
        for number in self.hash_table[2]:
            if (number != None):
                print(number)