import os
import function
import decorations
import settings

import space


def choice_edit():
    if (len(space.room) == 1):
        print("\tBrak adresow i notatek!")
        return
    decorations.ui()
    Choice = [
        'zobacz notatki',
        'dodaj notatke',
        'usun notatke'
    ]

    for index, mode in enumerate(Choice):
        print('\t', index+1, mode)

    your_choice = input("Co chcesz zrobic? ")

    if(your_choice == '1'):             #display note
        os.system('CLS')
        function.display()
    elif (your_choice == '2'):          #add note
        os.system('CLS')
        function.add()
    elif (your_choice == '3'):              #remove address
        os.system('CLS')
        function.delete()
    else:
        print("Nie ma takiego wyboru!")
#####################- #Start of program -######################################

                                                    #Uploading a file
space.room = []
with open('address.txt') as f:
    space.room = eval(f.read())

                                                        #Welcome User
decorations.ui()
print("\n\tWITAJ W PROGRAMIE 'Organizer zlecen'\n")

#####################- #Main loop -################################################
        #Main loop
while(True):
    decorations.operations()
    option = input("\n\t\t >> Co chcesz zrobic? ")
    
    if(option == '1'):                  #edit note
        os.system('CLS')
        choice_edit()
    elif(option == '2'):                #note
        os.system('CLS')
        function.display()
    elif(option == '3'):                #edit address
        os.system('CLS')
        function.edit_rooms()
    elif (option == '4'):               #address
        os.system('CLS')
        decorations.menu_rooms(False)
    elif(option == '5'):
        print("Papa! Milego dnia!")
        break
    elif (settings.test_mode == True):                 #Just for testing
        if(option == '6'):
            print(space.room)
    else:
        print("nie ma takiego wyboru!")

#########################################################


