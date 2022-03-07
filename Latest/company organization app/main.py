import os
import function
import display
import time

import winsound
###winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
 #sound 14 The Hunter's Path from THE WITCHER 3: WILD HUNT - OFFICIAL SOUNDTRACK


#------------- loading and configuration  -----------#
f = open("save.txt", "r")
settings = eval(f.readline())
function.workers = eval(f.readline())
function.blacklist = eval(f.readline())
function.earned = int(f.readline())
function.orders = eval(f.readline())
function.archvAddrs = eval(f.readline())
function.archv = eval(f.readline())
f.close()
function.test_mode = settings[0]
function.new_user = settings[1]
function.login = settings[2]
function.password = settings[3]
function.company = settings[4]
function.attempt = settings[5]

#------display application launch ------------#
def start(z):
    if(z == 0):
        print(' ')
    elif(z%3 == 1):
        print('.')
    elif (z%7 == 2):
        print('..')
    elif (z % 11 == 3):
        print('...')
os.system('CLS')

if not function.test_mode:
    ready = 0
    li = 0
    while (ready <= 50):
        display.ui()
        print('\n#\t\tOrganizer zlecen\t\t#\n\n \t\tLoading program', end='')
        start(li)
        display.ui()
        ready += 5
        if (li < 4):
            li += 1
        else:
            li = 0
        time.sleep(0.15)
        os.system('CLS')

#----------first start-----------#
if (function.test_mode == False):
    if (function.new_user == True):
        print("\nWitaj w organizerze zlecen dla Twojej firmy")
        while function.setopt[4] == ' ':
            function.setopt[4] = input('\nNazwa Twojej firmy: ')
            function.save()
        function.setopt[3] = input("Utworz haslo, aby pracownik nie usunal sobie zadan: ")
        function.setopt[1] = False
        function.save()
    print('\n',function.company, ' Wita! Pora zabrac sie do pracy!')
    verified = False
    while (verified == False):
        check = input("Podaj haslo: ")
        if (check == function.password or check == function.setopt[3]):
            verified = True


def money():
    display.ui()
    print('\n\tTwoj przychod wynosi:', function.earned, '(bez wydatkow)')
    display.ui()




#-------------- MENU ---------------##
while(True):
    winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
    display.ui()
    print('\t\tOrganizer zlecen')
    display.primary()
    option = input('\n\t\t >> Wybierz opcje: ')
    function.save()

    if (option == '1'):  # add note
        os.system('CLS')
        function.add_orders()
    elif (option == '2'):  # note
        os.system('CLS')
        display.orders_menu()
    elif (option == '3'):  # workers
        os.system('CLS')
        display.employees_menu()
    elif (option == '4'):  # archive
        os.system('CLS')
        function.display_archiv()
    elif (option == '5'):  # revenue
        os.system('CLS')
        money()
    elif (option == '6'):  # settings
        os.system('CLS')
        check = input('Podaj haslo: ')
        if (check == function.password or check == function.setopt[3]):
            display.settings_ch()
        else:
            print('Zle haslo!')
    elif (option == '7'):
        print("Papa! Milego dnia!")
        break
    elif (function.test_mode == True):  # Just for testing
        if (option == '8'):
            print(function.workers)
            print(function.blacklist)
        if (option == '9'):
            print(function.orders)
    else:
        print("nie ma takiego wyboru!")