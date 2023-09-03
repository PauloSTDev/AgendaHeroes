import string
import csv

class AgendaHeroes:
    def __init__(self, size = 26):
        self.size = size
        self.table = [None] * size
        self.numbers_table = [None] * size
        self.total_items = 0
        self.alphabet = [(string.ascii_lowercase)]
   
    def hash_function(self, key):
        original_name = key
        key = key.lower()
        hash = ord(key[0]) - 97
        # print("index: {}:{} - value: {}".format(self.alphabet[hash].upper(),hash, original_name))
        return hash

    def insert(self, key, value):
            if self.total_items == self.size:
                print("Full table")
                return False
            index = self.hash_function(key)
            if index >= self.size:
                return print("Invalid Name")
            if self.table[index] is None:
                self.table[index] = key
                self.numbers_table[index] = value
            else:
                while self.table[index] is not None:
                    index += 1
                    if index == self.size:
                        index = 0
                self.table[index] = key
                self.numbers_table[index] = value
            self.total_items += 1
            return True
   
    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                return "{}, {}".format(self.table[index], self.numbers_table[index])
            index += 1
            if index == self.size:
                index = 0
            if index == original_index:
                return "Not in List"
        return "Not in list"

    def show_numbers_table(self):
        return print(self.numbers_table)

    def show_contacts_table(self):
        return print(self.table)
    
    def add_contacts_from_diary(self):
        # Abertura e leitura de arquivo de agenda
        arquivo = open("agenda.csv", "r")
        reader = csv.reader(arquivo)

        # Adiciona contatos até a Abigail
        for linha in reader:
            self.insert(linha[0], linha[1])
            if linha[0] == "Abigail Quinn":
                break
