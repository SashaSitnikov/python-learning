def add_contact(contacts, name, phone):
    contacts[name] = phone
    print('Контакт добавлен!\n')


def find_contact(contacts, name):
    return contacts.get(name)


def delete_contact(contacts, name):
    if name in contacts:
        contacts.pop(name)
        return True
    return False


def show_all_contacts(contacts):
    for name, phone in contacts.items():
        print(name, phone)
    print()


def main():
    contacts = {'Anna': '+79785930611'}

    while True:
        print('1. Добавить контакт')
        print('2. Найти контакт по имени')
        print('3. Удалить контакт')
        print('4. Показать все контакты')
        print('0. Выход')

        choice = input('Выберите действие: ')
        print()

        if choice == '1':
            name = input('Введите имя контакта: ')
            phone = input('Введите его номер телефона: ')
            add_contact(contacts, name, phone)

        elif choice == '2':
            name = input('Введите имя контакта: ')
            phone = find_contact(contacts, name)

            if phone is not None:
                print(phone, '\n')
            else:
                print('Контакт не найден!\n')

        elif choice == '3':
            name = input('Введите имя контакта: ')

            if delete_contact(contacts, name):
                print('Контакт удален!\n')
            else:
                print('Контакт не найден!\n')

        elif choice == '4':
            show_all_contacts(contacts)

        elif choice == '0':
            break

        else:
            print('Неверный выбор!\n')


main()
