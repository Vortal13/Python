# Задача №49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def show_menu():
    print('1. Распечатать справочник \n' 
          '2. Найти телефон по фамилии \n'
          '3. Изменить номер телефона \n'
          '4. Удалить запись \n'
          '5. Найти абонента по номеру телефона \n'
          '6. Добавить абонента в справочник \n'
          '7. Закончить работу', sep = '\n')
    choice=int(input("Введите номер команды: "))
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.csv')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию для поиска: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('Введите фамилию для поиска: ')
            new_number=input('Введите новый номер: ')
            print(change_number(phone_book,last_name,new_number))
            write_txt('phonebook.csv', phone_book)
        elif choice==4:
            lastname=input('Введите фамилию для удаления записи: ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('Введите номер телефона для поиска:  ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            # user_data=input('new data ')
            add_user(phone_book)
            write_txt('phonebook.csv',phone_book)

        choice=show_menu()

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.split(',')))    
           phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}')

def print_result(phone_book):
    for line in phone_book:
        print(line)

def find_by_lastname(phone_book, last_name):
    sorted = list(filter(lambda k: k['Фамилия'] == last_name, phone_book))
    return list(map(lambda k: k['Фамилия']+ ' ' + k['Имя']+ ' - ' + k['Телефон'], sorted))

def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        if last_name == phone_book[i]['Фамилия']:
            key, number = 'Телефон', new_number
            phone_book[i].update({key: number})
    return phone_book

def delete_by_lastname(phone_book,lastname):
    for i in range(0, len(phone_book)):
        if lastname == phone_book[i]['Фамилия']:
            del phone_book[i]
            write_txt('phonebook.csv',phone_book)
    return phone_book

def find_by_number(phone_book,number):
    sorted = list(filter(lambda k: k['Телефон'] == number, phone_book))
    return list(map(lambda k: k['Фамилия']+ ' ' + k['Имя'], sorted))

def add_user(phone_book):
    data = {}

    lastname = input("Введите фамилию: ")
    key, value = 'Фамилия', lastname
    data.update({key: value})

    fistname = input("Введите имя: ")
    key, value = 'Имя', fistname
    data.update({key: value})

    number = input("Введите номер телефона: ")
    key, value = 'Телефон', number
    data.update({key: value})

    characteristic = input("Введите описание: ")
    key, value = 'Описание', characteristic
    data.update({key: value})

    phone_book.append(data)
    return phone_book

work_with_phonebook()

