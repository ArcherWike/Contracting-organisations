import display
############# configuration variables #####################################
workers = []
blacklist = []
orders = {}
archvAddrs = []
archv = {}
earned = 0

test_mode = False
new_user = True
login = ' '
password = ' '
company = ' '
attempt = 3
setopt = [test_mode, new_user, login, password, company, attempt]
###########################################################################
## $saving data to file
def save():
    lines = [setopt, workers, blacklist, earned, orders, archvAddrs, archv]
    with open('save.txt', 'w') as f:
        for l in lines:
            f.write("%s\n"%l)

## $checking if a given variable can be of type int
#                   &returns True if yes or False if no
def confirmInt(x):
    try:
        int(x)
    except:
        return False
    else:
        return True

## $ask repeat user selection. Only y/n possible.
def ask(question):
    x = input(question)
    if(x == 'y'):
        return True
    elif(x == 'n'):
        return False
    else:
        print('Nie ma takiego wyboru\nCzy chcesz sprobowac ponownie? y/n: ')
        return ask(question)
#########################################
def add_blacklist(x, index):
    if(x == True):
        blacklist.append(workers[index])
    else:
        print('\n Jesli sie rozmyslisz zawsze mozesz w Archiwum to zmienic')

def want_term():
    display.teq()
    userepl = input("Czy chcesz dodac termin wykonania? ")
    if (userepl == '1'):
        return True
    elif (userepl == '2'):
        return False
    elif (userepl == '3'):
        print("Mozesz dodac termin wykonania, w ktorym masz wykonac notatke\nPomoze Ci to w organizacji zadan")
        return want_term()
    elif (userepl == '4'):
        return 'Exit'
    else:
        print(" Nie ma takiego wyboru! ")
        return want_term()

def check_term():
    certainly = input("Czy chcesz sprobowac ponownie? y/n")
    if (certainly == 'y'):
        return True
    elif (certainly == 'n'):
        return False


def term():
    data = str(input("Podaj termin wykonania 'rok-miesiac-dzien': "))
    d = data.find("-")
    if (d != -1):
        if (len(data) == 10):
            spli = data.split("-")
            try:
                int(spli[0])
                int(spli[1])
                int(spli[2])
            except:
                print("Zla data")
                if(check_term() == True):
                    return term()
                else:
                    return False
            else:
                if (len(spli[0]) == 4):
                    if ((len(spli[1]) == 2) and (int(spli[1]) <= 12)):
                        if (len(spli[2]) == 2 and int(spli[2]) <= 31):
                            return str(data)
                        else:
                            print("Zly dzien!")
                            if(check_term() == True):
                                return term()
                            else:
                                return False
                    else:
                        print("Zly miesiac!")
                        if (check_term() == True):
                            return term()
                        else:
                            print("Dodawanie notatki nie powiodlo sie! :C ")
                            return False
                else:
                    print("Zly rok!")
                    if (check_term() == True):
                        return term()
                    else:
                        print("Dodawanie notatki nie powiodlo sie! :C ")
                        return False
        else:
            print("Zla data! ")
            if (check_term() == True):
                return term()
            else:
                print("Dodawanie notatki nie powiodlo sie! :C ")
                return False
    else:
        print("Zla data! ")
        if (check_term() == True):
            return term()
        else:
            print("Dodawanie notatki nie powiodlo sie! :C ")
            return False
###################################################################################
#
#                           EMPLOYESS
####################################################################################
def see_employees(option):
    print('')
    if (len(workers) == 0):
        print("\nNie masz pracownikow")
    else:
        for ix, name in enumerate(workers):
            if (option == True):
                print(ix+1, name)
            else:
                print(name)
def add_employee():
    name = input("\nPodaj pracownika: ")
    if(name == ''):
        print('Pracownik musi miec imie')
        return
    if(name in blacklist):
        sentence = "Pracownik %s znajduje sie na Twojej czarnej liscie. Czy napewno chcesz go zatrudnic i usunac z czarnej listy? y/n"%name
        if (ask(sentence) == True):
            ix = blacklist.index(name)
            del blacklist[ix]
        else:
            print('Pracownik nie zostal dodany')
    if(name in workers):
        print("%s jest juz u ciebie zatrudniony! Podaj z nazwiskiem albo pseudonimem"%name)
        return add_employee()
    workers.append(name)
    save()

def delete_employee():
    if (len(workers) == 0):
        print("\nNie masz pracownikow!")
        return
    see_employees(True)
    adrs = input('Podaj numer pracownika do usuniecia: ')
    if(confirmInt(adrs) == False):
        repl_user = ask('Nie ma takiego wyboru! Czy chcesz sprobowac ponownie? y/n ')
        if (repl_user == True):
            delete_employee()
        else:
            return
    else:
        adrs = int(adrs)
        if(adrs in range(1, len(workers)+1)):
            repl_user = ask("Czy dodac pracownika %s na czarna liste? y/n " %(workers[adrs-1]))
            add_blacklist(repl_user, (adrs-1))
            for location in orders:
                for wor in orders[location]:
                    for x, name in enumerate(orders[location]):
                        if (workers[adrs-1] == orders[location][x]['Wykona']):
                            orders[location][x]['Wykona'] = 'Nie przydzielono'
            del workers[adrs-1]
            save()

def see_blacklist():
    print('\n----CZARNA LISTA-----')
    if len(blacklist) == 0:
        print('czarna lista jest pusta')
    else:
        for ix, name in enumerate(blacklist):
            print(name)
####################################################################################
#
#                            ORDERS
####################################################################################
def print_order(user_answ,index):
    print('\t\t--\tZlecenie\t--\n')
    print('\tklient: ', orders[user_answ][index]['Klient'])
    print('\tadres: ', user_answ)
    print('\ttermin wykonania: ', orders[user_answ][index]['Termin'])
    print('\twykonuje: ', orders[user_answ][index]['Wykona'])
    print('\tOpis zadania: ', orders[user_answ][index]['Opis'])
    print('')
    display.ui()

def display_order():
    if (len(orders) == 0):
        print('Brak zlecen')
    else:
        display.numerate_dict(orders, True)
        user_answ = input('Zlecenia z ktorego adresu chcesz zobaczyc: ')
        if (confirmInt(user_answ) == True):
            user_answ = int(user_answ)
            if (user_answ in range(0, len(orders) + 1)):
                if (user_answ in range(1, len(orders))):
                    for ix, address in enumerate(orders):
                        if (user_answ == ix + 1):
                            location = address
                            print(address)
                            continue
                    for ix, loc in enumerate(orders[location]):
                            print_order(location, ix)
                else:
                    for adr in orders:
                        for ix, loc in enumerate(orders[adr]):
                                print_order(adr, ix)
            else:
                print('Nie ma takiego wyboru')
        else:
            print('Nie ma takiego wyboru')

def list_employee(ask_user):
    print('\nPrzydziel kogos do zlecenia')
    if (len(workers) == 0):
        print("\nNie masz pracownikow")
    if (ask_user == True):
        print('0', 'Nie przydzielaj, dodam pozniej')
        print('1', 'Przydziel mnie')
    for ix, name in enumerate(workers):
        print(ix+2, name)
    user_answ = input('\n\t >>> Wybierz opcje lub podaj pracownika: ')
    if (user_answ == '0' or user_answ == 'Nie przydzielaj, dodam pozniej'):
        return 'Nie przydzielono'
    elif(user_answ == '1' or user_answ == 'Przydziel mnie'):
        return 'ja'
    else:
        if (confirmInt(user_answ) == True):
            user_answ = int(user_answ)-2
        else:
            try:
                workers.index(user_answ)
            except:
                print('Nie ma takiego pracownika!')
                x = ('Czy chcesz sprobowac przydzielic pracownika ponownie? y/n')
                if (ask(x) == True):
                    return list_employee(True)
                else:
                    return False
            else:
                user_answ = workers.index(user_answ)
        if (user_answ in range(0,len(workers))):
            return workers[user_answ]
        else:
            print('Nie ma takiego pracownika!')
            x = ('Czy chcesz sprobowac przydzielic pracownika ponownie? y/n')
            if (ask(x) == True):
                return list_employee(True)
            else:
                return False


def add_orders():
    customer = input('\nPodaj imie i nazwisko klienta lub nazwe jego firmy: ')
    location = input("\nPodaj adres, na ktorym wykonac zlecenie %s: " %customer)
    description = input('\nOpisz zlecenie: ')
    deadline = 'Nie podano'
    user_answ = want_term()
    if (user_answ == True):
        deadline = term()
    elif (user_answ == 'Exit'):
        return
    user_answ = list_employee(True)
    if (user_answ == False):
        return
    else:
        worker = user_answ
    new = {'Klient': customer, 'Termin': deadline, 'Wykona': worker, 'Opis': description}
    for x in orders:
        if(x == location):
            orders[location].append(new)
            save()
            return
    orders[location] = [new]
    save()

def check_money():
    money = input('Ile dostales za zlecenie lub [e] aby wyjsc: ')
    if(money == 'e'):
        return False
    else:
        x = confirmInt(money)
        if (x == True):
            global earned
            earned += int(money)
            return True
        else:
            print('Nie prawidlowa wartosc! \nWpisz liczbe lub [e] aby wyjsc')
            return check_money()

def close_order():
    if (len(orders) == 0):
        print('Brak zlecen')
        return
    check = display.see_address_customer(True, orders)
    user_answ = display.ask_see_address('Podaj numer zlecenia do zakmniecia', check)
    if (user_answ == False):
        return
    else:
        display.ui()
        if (len(orders[user_answ]) == 1):
            if (check_money() == True):
                archv[user_answ] = orders[user_answ]
                del orders[user_answ]
                save()
            else:
                print('Zamykanie zlecenia nie powiodlo sie!')
                return
        else:
            for ix in range(1, len(orders[user_answ]) + 1):
                print(ix, 'Adres:', user_answ, ',\tKlient:', orders[user_answ][0]['Klient'])
            index = input('Podaj ktore zlecenie zamknac: ')
            if(confirmInt(index) == True):
                index = int(index)
                if (index in range(1, len(orders[user_answ])+1)):
                    if check_money() == True:
                        archv[user_answ] = orders[user_answ][index - 1]
                        del orders[user_answ][index - 1]
                        save()
                    else:
                        print('Zamykanie zlecenia nie powiodlo sie!')
                else:
                    print('Nie ma takiego wyboru!')
            else:
                print('Nie ma takiego wyboru!')

def remove_order():
    if (len(orders) == 0):
        print('Brak zlecen')
    else:
        display.numerate_dict(orders, True)
        user_answ = input('Podaj numer zlecenia do usuniecia: ')
        if (confirmInt(user_answ) == True):
            user_answ = int(user_answ)
            if (user_answ in range(0, len(orders) + 1)):
                if (user_answ in range(1, len(orders) + 1)):
                    for ix, address in enumerate(orders):
                        if (user_answ == ix + 1):
                            location = address
                            print(address)
                            continue
                    if (len(orders[location]) == 1):
                        del orders[location]
                    else:
                        display.numerate_dict(orders[location], True)
                        index = input('Podaj ktore zlecenie usunac: ')
                        if (index in range(1, (orders[user_answ]) + 1)):
                            del orders[user_answ][index - 1]
                        else:
                            print('Nie ma takiego wyboru!')
                            return
                else:
                    question = 'Czy napewno usunac wszystkie zlecenia? y/n'
                    if (ask(question) == True):
                        for address in orders:
                            del orders[address]
            else:
                print('Nie ma takiego wyboru')
        else:
            print('Nie ma takiego wyboru')

def edit_sth_in_order(address, index):
    option = display.edit()
    if (option == 'term'):
        user_answ = want_term()
        if (user_answ == True):
            deadline = term()
        elif (user_answ == False):
            return
        else:
            return
        orders[address][index]['Termin'] = deadline
    elif (option == 'worker'):
        user_answ = list_employee(True)
        if (user_answ == 'exit'):
            return
        else:
            if(user_answ == 0):
                orders[address][index]['Wykona'] = 'Nie przydzielono'
            elif (user_answ == 1):
                orders[address][index]['Wykona'] = 'ja'
            else:
                orders[address][index]['Wykona'] = user_answ
    elif (option == 'description'):
        description = input('\nOpisz zlecenie: ')
        if(description != ''):
            orders[address][index]['Opis'] = description
        else:
            print('Opis nie moze zostac pusty!')
    save()

def edit_order():
    if (len(orders) == 0):
        print('Brak zlecen')
    else:
        display.numerate_dict(orders, False)
        user_answ = input('Podaj numer zlecenia do edytowania: ')
        if (confirmInt(user_answ) == True):
            user_answ = int(user_answ)-1
            if (user_answ in range(0, len(orders))):
                for ix, address in enumerate(orders):
                    if (user_answ == ix):
                        location = address
                if (len(orders[location]) > 1):
                    display.numerate_dict(orders[location], False)
                    index = input('Podaj ktore zlecenie edytowac: ')
                    if (confirmInt(index) == True):
                        index = int(index) - 1
                    if (index in range(1, len(orders[location]))):
                        edit_sth_in_order(location, (index))
                    else:
                         print('Nie ma takiego wyboru!')
                         return
                else:
                    edit_sth_in_order(location, 0)

            else:
                print('Nie ma takiego wyboru')
        else:
            print('Nie ma takiego wyboru')
    save()
##########---------------------- Archive -----------------------------------###################
def print_archv(user_answ,index):
    print('\t\t--\tZlecenie\t--\n')
    print('\tklient: ', archv[user_answ][index]['Klient'])
    print('\tadres: ', user_answ)
    print('\ttermin wykonania: ', archv[user_answ][index]['Termin'])
    print('\twykonuje: ', archv[user_answ][index]['Wykona'])
    print('\tOpis zadania: ', archv[user_answ][index]['Opis'])
    print('')
    display.ui()

def display_archiv():
    display.ui()
    print('\t\t\tARCHIWUM ZAMKNIETYCH ZLECEN')
    display.ui()
    if(len(archv) == 0):
        print('Brak zlecen w archiwum')
    else:
        for address in archv:
            if (len(archv[address]) == 1):
                print_archv(address, 0)
            else:
                for ix in range(0, len(archv[address])-1):
                    print(ix)
                    print_archv(address, ix)
######################################################## SETTINGS ###############
def change_password():
    global password
    passw = input('Wprowadz haslo: ')
    if passw == setopt[3] or passw == password:
        x = input('Wprowadz nowe haslo: ')
        setopt[3] = x
        password = x
    else:
        if(setopt[5] == 1):
            print('Pozostala 1 proba. Jesli wpiszesz zle haslo zablokujesz program!')
        print("Zle haslo, pozostaly %s proby! "%setopt[5])
        setopt[5] = setopt[5] - 1
        if (setopt[5] == 0):
            exit()
def change_name():
    global company
    company = input('Podaj nazwe firmy: ')
    setopt[4] = company
    save()
def reset_app():
    global setopt
    if (ask('Czy napewno usunac wszystkie dane z aplikacji? Nie bedzie mozna przywrocic! y/n') == True):
        setopt = [False, True, ' ', ' ', ' ', 3]
        workers.clear()
        blacklist.clear()
        global earned
        earned = int(0)
        orders.clear()
        archv.clear()
        save()
        exit()