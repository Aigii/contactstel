import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1] [0]}? (y/n)')
    if confirm.lower()=='y':
        del_contact = phone_book.pop(id-1)

def change_contact():
    global phone_book
    i = view.input_change_contact()
    for id, contact in enumerate(phone_book):
        if id == i:
            print('Введите новое имя контакта: ')
            new_name = input()
            print('Введите новой номер контакта: ')
            new_phone = input()
            comment = input('Введите ком контактая: ')
            phone_book[id-1] = [new_name, new_phone, comment]

def find_contact():
    global phone_book
    name = view.input_find_contact()
    data = next(filter(lambda x: x[0] == name, phone_book), None)
    print(*data)




