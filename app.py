documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
    }


"""Task 1."""

def get_name(number: str) -> str:
    """Find the owner's name in a document."""
    for document in documents:
        for value in document.values():
            if number == value:
                return document['name']
    else:
        return 'Документ не найден'

def get_shelf_number(shelf_number: str) -> str:
    """Find the shelf number on a document."""
    for number, documents in directories.items():
        for document in documents:
            if shelf_number == document:
                return number
    else:
        return 'Документ не найден'

def get_all_documents() -> list:
    """Documents list."""
    documents_list = []
    for document in documents:
        documents_list.append([document['type'], document['number'], document['name']])
    return documents_list

def add_document(type: str, number: str, name: str, shelf: str) -> str:
    """Add a new document to the shelf."""
    for document in documents:
        if number in document.values():
            return 'Документ уже существует'

    for k in directories.keys():
        if shelf == k:
            directories[k].append(number)
            break
    else:
        return 'Номер полки не найден'

    documents.append({"type": type, "number": number, "name": name})

    return 'добавлен документ на полку ' + shelf


"""Task 2."""

def del_document(number: str) -> str:
    """Remove the document from the list and from the shelf."""
    for value in directories.values():
        if number in value:
            value.remove(number)

    for document in documents:
        for value in document.values():
            if number == value:
                documents.remove(document)
                return 'Документ ' + number + ' удалён'
    else: 
        return 'Документ не найден'

def move_document(number: str, new_shelf: str) -> str:
    """Move document to another shelf"""
    if new_shelf not in directories.keys():
        return 'Данной полки не существует'
    
    for key, value in directories.items():
        if number in value:
            if key == new_shelf: 
                return 'Документ итак уже на этой полке!'
            value.remove(number)
            break
    else: return 'Номер документа не найден'

    for k in directories.keys():
        if new_shelf == k:
            directories[k].append(number)
            
    return 'Документ перемещён'

def add_shelf(new_shelf: str) -> str:
    """Add a new shelf."""
    if new_shelf in directories.keys():
        return 'Данная полка уже существует'

    directories.update({new_shelf: []})
    return 'Полка ' + new_shelf + ' добавлена'

def get_help():
    print('Мои комманды:')
    print('p - найти имя владельца по документу')
    print('s - найти номер полки по документу')
    print('l - список всех документов')
    print('a - добавить новый документ на полку')
    print('d - удалить документ из списка и с полки')
    print('m - переместить документ на другую полку')
    print('h - помощь по командам')
    print('as - добавить новую полку')
    print('q - пойти домой')


def main():
    print('Здравствуйте, я Ваш помощник по поиску документов')
    get_help()
    
    while True:

        command = input('--> ').lower().strip()

        if command == 'h':
            get_help()
        
        elif command == 'q':
            print('До свидания, хорошего дня. Жду Вас ещё!')
            break

        elif command == 'p':
            document_number = input('Введите номер документа: ')
            print('ФИО владельца - ' + get_name(document_number))

        elif command == 's':
            document_number = input('Введите номер документа: ')
            print('Номер полки - ' + get_shelf_number(document_number))

        elif command == 'l':
            for v in get_all_documents():
                print(*v)

        elif command == 'a':
            document_type = input('Введите тип документа: ')
            number = input('Введите номер документа: ')
            name = input('Введите ФИО владельца: ')
            shelf = input('Введите номер полки: ')
            print(add_document(document_type, number, name, shelf))

        elif command == 'd':
            number = input('Введите номер документа: ')
            print(del_document(number))

        elif command == 'm':
            number = input('Введите номер документа: ')
            new_shelf = input('Введите полку, куда нужно переместить документ: ')
            print(move_document(number, new_shelf))
        
        elif command == 'as':
            new_shelf = input('Введите номер новой полки: ')
            print(add_shelf(new_shelf))

        else:
            print('Ошибка комманды. Для получения справки, введите - h')


if __name__ == '__main__':
    main()