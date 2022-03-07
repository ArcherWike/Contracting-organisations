import function
import os

def ui():
    print("-" * 50)

#------------------displaying the main menu:
def primary():
    ui()
    menu = [
        'Dodaj zlecenie',
        'Zlecenia',
        'Pracownicy',
        'Archiwum',
        'Przychod',
        'Ustawienia',
        'Wyjdz'
    ]
    for ix, name in enumerate(menu):
        print("\t", ix + 1, name)
    ui()

#-----------displaying and optionin menu workers
def employees_menu():
    ui()
    menu =  [
        'Zobacz swoj personel',
        'Dodaj pracownika',
        'Usun pracownika',
        'Zerknij na czarna liste pracownikow'
    ]
    for ix, name in enumerate(menu):
        print("\t", ix + 1, name)
    ui()
    option = input("\n\t\t>>Wybierz opcje: ")
    if (option == '1'):  # see employees
        os.system('CLS')
        function.see_employees(False)
    elif (option == '2'):  # add employee
        os.system('CLS')
        function.add_employee()
    elif (option == '3'):  # delete employee
        os.system('CLS')
        function.delete_employee()
    elif (option == '4'):  # see blacklist
        os.system('CLS')
        function.see_blacklist()
    else:
        print("Nie ma takiego wyboru!")
        repeat = input("Czy chcesz sprobować ponownie? y/n")
        if (repeat == 'y'):
            employees_menu()
        elif (repeat == 'n'):
            return
        else:
            print("Nie ma takiego wyboru!")
            return
#------------menu orders
def orders_menu():
    ui()
    menu = [
        'Zobacz zlecenia',
        'Dodaj zlecenie',
        'Usun zlecenie',
        'Edytuj',
        'Zakoncz zlecenie'
    ]
    for ix, name in enumerate(menu):
        print("\t", ix + 1, name)
    ui()
    option = input("\n\t\t>>Wybierz opcje: ")
    if (option == '1'):  # see orders
        os.system('CLS')
        function.display_order()
    elif (option == '2'):  # add orders
        os.system('CLS')
        function.add_orders()
    elif (option == '3'):  # delete orders
        os.system('CLS')
        function.remove_order()
    elif (option == '4'):  # edit orders
        os.system('CLS')
        function.edit_order()
    elif (option == '5'):  # edit orders
        os.system('CLS')
        function.close_order()
    else:
        print("Nie ma takiego wyboru!")
        repeat = input("Czy chcesz sprobować ponownie? y/n")
        if (repeat == 'y'):
            employees_menu()
        elif (repeat == 'n'):
            return
        else:
            print("Nie ma takiego wyboru!")
            return

def numerate_dict(dict, option):
    ui()
    if (option == True):
        print('0', 'wszystkie zlecenia')
    for ix, address in enumerate(dict):
        print(ix+1, address)
    ui()

def ask_see_address(question, chek):
    user = input(question)
    if (function.confirmInt(user) == True):
        user = int(user)
    if (user == 0):
        return 'all'
    elif (user in range(0, len(chek) + 1)):
        return chek[user - 1]
    else:
        print('Nie ma takiego wyboru')
        return False

def see_address_customer(z, dictionary):
    print('')
    chek = []
    index = 0
    if (z == True):
        print(index, 'wszystkie zlecenia')
    index += 1
    for adress in dictionary:
        print('')
        chek.append(adress)
        if(len(dictionary[adress]) == 1):
            print(index,'Adres:',adress, ',\tKlient:', dictionary[adress][0]['Klient'])
            index += 1
        else:
            for x in range(0, len(dictionary[adress])):
                print(dictionary)
                print(index, 'Adres:', adress, ',\tKlient:', dictionary[adress][x]['Klient'])
    return chek

def edit():
    ui()
    menu = [
        'Termin wykonania',
        'Zmienic przydzielonego pracownika',
        'Opis zadania'
    ]
    for ix, name in enumerate(menu):
        print("\t", ix + 1, name)
    ui()
    option = input("\n\t\t>>Wybierz opcje: ")
    if (option == '1'):
        return 'term'
    elif (option == '2'):
        os.system('CLS')
        return 'worker'
    elif (option == '3'):
        os.system('CLS')
        return 'description'
    else:
        print("Nie ma takiego wyboru!")
        repeat = input("Czy chcesz sprobować ponownie? y/n")
        if (repeat == 'y'):
            return edit()
        elif (repeat == 'n'):
            return False
        else:
            print("Nie ma takiego wyboru!")
            return False

def teq():
    ui()
    quterm = ['Dodaj termin wykonania',
              'Nie dodawaj',
              'O co chodzi?',
              'Wroc do menu'
              ]
    for x, an in enumerate(quterm):
        print("\t", x + 1, an)
    ui()

###
def settings_ch():
    ui()
    menu = [
        'Zmien haslo',
        'Zmien nazwe firmy',
        'usun wszystkie dane z aplikacji'
    ]
    for ix, name in enumerate(menu):
        print("\t", ix + 1, name)
    ui()
    option = input("\n\t\t>>Wybierz opcje: ")
    if (option == '1'):
        function.change_password()
    elif (option == '2'):
        os.system('CLS')
        function.change_name()
    elif (option == '3'):
        os.system('CLS')
        function.reset_app()
    else:
        print("Nie ma takiego wyboru!")
        repeat = input("Czy chcesz sprobować ponownie? y/n")
        if (repeat == 'y'):
            return settings_ch()
        elif (repeat == 'n'):
            return False
        else:
            print("Nie ma takiego wyboru!")
            return False