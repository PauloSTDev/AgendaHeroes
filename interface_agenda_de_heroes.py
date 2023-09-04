
from agenda_de_herois import AgendaHeroes

heroes_hash = AgendaHeroes()

choice = 0

print("Bem vindo ao Sistema da Agenda do Clube Secreto de Super-Heróis")

while (True):
    print("""
    1. Adicionar Super-Heróis
        1.2. Importar da lista de Agenda
    2. Buscar Super-Heróis
    3. Mostrar todos os Super-Heróis pela letra
        3.1. Mostrar os nomes na lista de contatos
        3.2. Mostrar os numeros de contatos
    4. Remover Super-Herói
    5. Sair
    
    """)

    print("Escolha uma Opção: ")
    choice = input()

    if choice == '1':
        print("Adicione o nome do contato: ")
        contact = input()
        print("Adicione seu número: ")
        number = input()
        heroes_hash.insert(contact, number)

    elif choice == '1.2':
        heroes_hash.add_contacts_from_diary()

    elif choice == '2':
        print("Digite o nome do contato: ")
        contact = input()
        heroes_hash.search(contact)

    elif choice == '3':
        print("Digite a primeira letra para pesquisa: ")
        word = input()
        heroes_hash.searchByWord(word)
        
    elif choice == "3.1":
        heroes_hash.showNames()

    elif choice == "3.2":
        heroes_hash.showNumbers()

    elif choice == '4':
        print("Digite o nome do contato para excluir: ")
        contactToDelete = input()
        heroes_hash.delete(contactToDelete)

    elif choice == '5':
        break
