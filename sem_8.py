# 1. Создание файла:
#     - открываем файл на дозаписть
# 2. Добавление контакта:
#     - запросить у пользователя нвоый контакт
#     - открыть файл на дозапись
#     - добавить новый контакта
# 3. Вывод данных на экран:
#     - открыть файл на чтение
#     - считать файл
#     - вывести на экран
# 4. Поиск контакта
#     - выбор варианта поиска
#     - запросить данных для поиска
#     - открыть файл на чтение
#     - считать данные файла, сохранить их в переменную
#     - осуществление поиска контакта
#     - вывести на экран найденный контакт
# 5. Создание UI:
#     - вывести меню на экран
#     - зарпосить у пользователя вариант действия
#     - запустить соответствующую функцию
#     - осуществить возможность выхода из программы

def input_surname():
    return input('введите фамилию конаткта: ')

def input_name():
    return input('введите имя конаткта: ')

def input_patronymic():
    return input('введите отчество конаткта: ')

def input_phone():
    return input('введите телефон контакта: ')

def input_adress():
    return input('введите адрес(город) контакта: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    return f'{surname} {name} {patronymic}: {phone}\n{adress}\n\n'

def add_contact():
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(create_contact())
    

def print_contacts():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n,contact in enumerate(contacts_list,1):
        print(n,contact)


def search_contact():
    print(
            'Возможные варианты:\n'
            '1. По фамилии\n'
            '2. По имени\n'
            '3. По отчеству\n'
            '4. по телефону\n'
            '5. по адресу(городу)\n'
        )
    var = input('Выберите вариант поиска: ')
    while var not in ('1','2','3','4','5'):
        print('Некорректный ввод')
        var = input('выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ')
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    list_contacts = contacts_str.rstrip().split('\n\n')
    
    for str_contact in list_contacts:
        lst_contact = str_contact.replace(':','').split()
        if search in lst_contact[i_var]:
            print(str_contact)

def copy_line():
    line_number = int(input('Введите номер строки: '))
    with open("phonebook.txt", 'r', encoding='utf-8') as file1:
        lines1 = file1.read()
    line_list = lines1.rstrip().split('\n\n')
    
    for n,contact in enumerate(line_list,1):
        if n == line_number:
            print(n,contact)
            with open("phonebook_copy.txt", 'a+', encoding='utf-8') as file2:
                file2.write(contact)
                file2.write('\n')


    

def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass
    var = 0
    while var != 4:
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Перенос строки\n'
            '5. Выход\n'
        )
        print()
        var = input('Выберите вариант действия: ')
        while var not in ('1','2','3','4'):
            print('Некорректный ввод')
            var = input('выберите вариант действия: ')
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_line()    
            case '5':
                print('конец')
        print()


if __name__ == '__main__':
    interface()