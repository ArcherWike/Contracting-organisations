import decorations
import space

#--------------------------#   Input testing   #-------------------------------#

            
def testing(x):
    for num in range(0, len(space.room)):
        if(x == str(num)):
            return True
    return False



#------------------------------- GENERAL FUNCTION ------------------------------#





def edit_rooms():
    decorations.rooms_option()
    space_option = input("Co chcesz zrobic? ")
    if(space_option == '1'):                                              #display address
        decorations.menu_rooms(False)
    elif(space_option == '2'):                                            #add new address
        name_space = str(input('podaj adres do dodania: '))
        space.room.append([name_space])
    elif(space_option == '3'):                                            #remove address
        if(len(space.room) == 1):
            print("Brak adresow!")
            return
        decorations.menu_rooms(True)
        spaceDel = input("Numer adresu do usuniecia: ")
        if (testing(spaceDel)):
            spaceDel = int(spaceDel)
        else:
            print("Nie ma takiego adresu!")
            return
        #################################
        if(spaceDel in range(1, len(space.room))):
            del space.room[spaceDel]
        elif(spaceDel == 0):
            certainly = input("Napewno usunac wszystkie adresy? y/n")
            if (certainly == 'y'):
                for index in range(1, len(space.room)):
                    del space.room[1]
            elif (certainly == 'n'):
                return
            else:
                print("Nie ma takiego wyboru!")
        else:
            print("Nie ma takiego wyboru!")

    else:
        print("Nie ma takiego wyboru")




                                #   Display note   #
def display():
    if(len(space.room) == 1):
        print("Brak adresow i notatek!")
        return
    decorations.menu_rooms(True)
    num = input("zadania z ktorego adresu chcesz zobaczyc? ")

    if(testing(num)):
        num = int(num)
    else:
        print("Nie ma takiego adresu!")
        return

    if (num in range(1,len(space.room))):
        print("Adres " + str(space.room[num][0].capitalize()) + ": ")
        if(len(space.room[num]) > 1):
            decorations.display_notes(num)
        else:
            print("\n\t<Brak notatek>")
    elif(num == 0):
        for i in range(1, len(space.room)):
            print("--------------\n", (space.room[i][0])+": ")
            if(len(space.room[i]) > 1):
                for y in range(1, len(space.room[i])):
                    print('\t', space.room[i][y])
            else:
                print("\n\t<Brak notatek>")
        print("--------------")
    else:
        print("\nTaki adres nie istnieje")
    



                                #   Add note   #
def add():
    if((len(space.room) == 1)):
        print("Brak adresow!\n Nie masz gdzie przypisac notatki!\n Nie martw sie to zostalo przewidziane, ten program sie nie wysypie!")
        return
    decorations.menu_rooms(True)
    num_where_add = input("do jakiego adresu przypisac notatke? ")
    
    if(testing(num_where_add)):
        num_where_add = int(num_where_add)
    else:
        print("Nie ma takiego adresu!")
        return

    content = input("Podaj tresc notatki: ")
    
    if(num_where_add in range(1,11)):
        space.room[num_where_add].append(content)
    elif(num_where_add == 0):
        for x in range(1, 11):
            space.room[x].append(content)
    else:
        print("Taki pokoj nie istnieje!")



                                #   Delete note    #
def delete():
    if ((len(space.room) == 1)):
        print("Brak adresow!\n Nie masz czego usunac!\n Nie martw sie to zostalo przewidziane, ten program sie nie wysypie!")
        print("Najpierw dodaj adres!")
        return
    decorations.menu_rooms(True)
    
    delRoom = input("Z jakiego pokoju usunac notatke? ")
    if(testing(delRoom)):
        delRoom = int(delRoom)
    else:
        print("Nie ma takiego pokoju!")
        return
        

    if (delRoom in range(1, len(space.room))):
        print("Pomieszczenie " + str(space.room[delRoom][0])+'\n')
        if (len(space.room[delRoom]) < 2):
            print("Brak notatek!")
            return
        else:
            print("\t 0 Usun wszystkie")

        decorations.display_notes(delRoom)
        
        num = input("Jaki numer ma notatka do usuniecia? ")
  
        if(testing(num)):
            num = int(num)
        else:
            print("nie ma takiej notatki!")
        if (num in range(1,len(space.room[delRoom]))):
            del space.room[delRoom][num]
            print("usunieto pomyslnie ;)")
            
        elif(num == 0):
            certainly = input("Napewno usunac wszystkie notatki? y/n")
            if(certainly == 'y'):
                for index in range(1, len(space.room[delRoom])):
                    del space.room[delRoom][1]
            elif(certainly == 'n'):
                return
            else:
                print("Nie ma takiego wyboru!")
        else:
            print("Nie ma takiego wyboru!")
    elif(delRoom == 0):
        certainly = input("Napewno usunac wszystkie notatki? y/n")
        if(certainly == 'y'):
            for index in range(1, len(space.room)):
                for z in range(1, len(space.room[index])): 
                    del space.room[index][1]
        elif(certainly == 'n'):
            return
        else:
            print("Nie ma takiego wyboru!")
    else:
        print("taki pokoj nie istnieje!")
