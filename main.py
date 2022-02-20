import os
import function
import decorations
import space        # its delete

def choice_edit():
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

#####################- #Main loop -######################################


decorations.ui()
print("\n\tWITAJ W PROGRAMIE NOTATNIK WOŹNEGO\n")


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
    else:
        print("nie ma takiego wyboru!")

#########################################################


