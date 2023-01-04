import phone_book as pb

def main_menu():
    print('Выберите команду меню:')
    print('1. Показать тел книгу')
    print('2. Загрузить тел книгу')
    print('3. Сохранить тел книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range(1, 8) or choice==0:
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')


def print_phone_book():
    phone_book = pb.get_phone_book()
    print()
    if len(phone_book) < 1:
        print('Тел книга пуста\n')
    else:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    print()

def input_new_contact():

    name = input('Введите имя контакта: ')
    phone = input('Введите тел контакта: ')
    comment = input('Введите ком контактая: ')
    new_contact = [name, phone, comment]
    return new_contact


def input_remove_contact():
    print()
    print_phone_book()
    id = int(input('Введите ID контакта для удаления: '))
    return id

def input_change_contact():
    print()
    print_phone_book()
    idd = int(input(f'Введите id контакта: '))
    return idd

def input_find_contact():
    n = input('Введите имя: ')
    name=str.title(n)
    return name

