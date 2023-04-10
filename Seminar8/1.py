def print_menu():
    print("""
    1 - Открыть файл 
    2 - Найти контакт
    3 - Создать контакт
    4 - Изменить контакт
    5 - Удалить контакт 
    6 - Выход""")


def insert():
    with open(file_path, 'a', encoding='UTF-8') as open_book:
        add_f = (input('Введите Фамилию: ').title())
        add_n = (input('Введите Имя: ').title())
        add_phone = (input('Введите телефон: ').title())
        new_line = add_f + ' '+add_n + ' ' + add_phone
        open_book.writelines(f'\n{new_line}')
        print(new_line)


def search():
    with open(file_path, 'r', encoding='UTF-8') as open_book:
        search_inf = (input('Введите информацию для поиска: ').title())
        for line in open_book:
            if search_inf in line:
                print(line)


def remove_contact():
    with open(file_path, 'r', encoding="UTF-8") as open_book:
        r = input('Введите Имя или Фамилию для удаления: ')
        lines = open_book.readlines()
        with open(file_path, 'w', encoding="UTF-8") as open_book:
            for line in lines:
                if r in line:
                    print("Контакт удален")
                else:
                    print(line)
                    open_book.write(line)


def edit():
    with open(file_path, 'r', encoding="UTF-8") as open_book:
        search_inf = (input('Введите информацию для поиска: ').title())
        with open(file_path, 'w', encoding='UTF-8') as open_book:
            for line in search_inf:
                if search_inf in line:
                    print(line)
                    add_f = (input('Введите фамилию: ').title())
                    add_n = (input('Введите Имя: ').title())
                    add_phone = (input('Введите телефон: ').title())
                    new_line = add_f + ' '+add_n + ' ' + add_phone + '\n'
                    line = line.replace(line, new_line)
                open_book.writelines(line)


def read_all():
    with open(file_path, 'r', encoding='UTF-8') as open_book:
        print()
        for line in open_book:
            print(line)


def tasks(task):
    if task > 6:
        print('Неверный запрос')
    if task == 6:
        print('До встречи:)')
    else:
        match task:
            case 1:
                read_all()
                print_menu()
                tasks(int(input('Введите номер действия: ')))
            case 2:
                search()
                print_menu()
                tasks(int(input('Введите номер действия: ')))
            case 3:
                insert()
                print_menu()
                tasks(int(input('Введите номер действия: ')))
            case 4:
                edit()
                print_menu()
                tasks(int(input('Введите номер действия: ')))
            case 5:
                remove_contact()
                print_menu()
                tasks(int(input('Введите номер действия: ')))


file_path = 'phone_book.txt'
print_menu()
tasks(int(input('Введите номер действия: ')))
