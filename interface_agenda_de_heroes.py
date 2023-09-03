
from agenda_de_herois import AgendaHeroes


heroes_hash = AgendaHeroes()

# Adiciona contatos pela agenda
heroes_hash.add_contacts_from_diary()
heroes_hash.show_numbers_table()
heroes_hash.show_contacts_table()
print("""Bem vindo ao Sistema da Agenda do Clube Secreto de Super-Heróis

1. Adicionar Super-Heróis
2. Buscar Super-Heróis
3. Mostrar todos os Super-Heróis pela letra
4. Remover Super-Herói
5. Sair

Escolha uma Opção: """)
choice = input()

print("Adicione o nome do contato")
contact = input()
print("Adicione seu número")
number = input()
heroes_hash.insert(contact, number)
heroes_hash.show_numbers_table()
heroes_hash.show_contacts_table()