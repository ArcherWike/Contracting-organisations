import decorations
import space



def update():
    file = open('address.txt', 'w')
    file.writelines(str(space.room))
    file.close()

#--------------------------#   Input testing   #-------------------------------#

            
def testing(x):
    for num in range(0, len(space.room)):
        if(x == str(num)):
            return True
    return False




def term():
    data = str(input("Podaj termin wykonania 'rok-miesiac-dzien': "))
    d = data.find("-")
    if (d != -1):
        if (len(data) == 10):
            spli = data.split("-")
            if (len(spli[0]) == 4):
                if ((len(spli[1]) == 2) and (int(spli[1]) <= 12)):
                    if (len(spli[2]) == 2 and int(spli[2]) <= 31):
                        return data

                    else:
                        print("Zly dzien!")
                        return False
                else:
                    print("Zly miesiac!")
                    return False
            else:
                print("Zly rok!")
                return False
        else:
            print("Zla data! ")
            return False
    else:
        print("Zla data! ")
        return False


#------------------------------- GENERAL FUNCTION ------------------------------#



                        #__sorting function
def sortek(index):
    if (len(space.room[index]) == 1):
        return
    else:
        for z in range(2, len(space.room[index])*2):
            for y in range(2, len(space.room[index])):
                print(space.room)
                print('y is: ',y)
                first_term = space.room[index][y].split(" |term: ")
                second_term = space.room[index][y - 1].split(" |term: ")
                print('1: ',second_term[1])
                print('2: ',first_term[1])
                s = second_term[1].split("-")
                f = first_term[1].split("-")

                if (s[0] < f[0]):
                    wait = space.room[index][y]
                    space.room[index][y] = space.room[index][y - 1]
                    space.room[index][y - 1] = wait
                    break
                elif (s[0] == f[0]):
                    if (s[1] < f[1]):
                        wait = space.room[index][y]
                        space.room[index][y] = space.room[index][y - 1]
                        space.room[index][y - 1] = wait
                        break
                    elif (s[1] == f[1]):
                        if (s[2] < f[2]):
                            wait = space.room[index][y]
                            space.room[index][y] = space.room[index][y - 1]
                            space.room[index][y - 1] = wait
                            break




def edit_rooms():
    decorations.rooms_option()
    space_option = input("Co chcesz zrobic? ")
    if(space_option == '1'):                                              #display address
        decorations.menu_rooms(False)
    elif(space_option == '2'):                                            #add new address
        name_space = str(input('podaj adres do dodania: '))
        space.room.append([name_space])
        update()
    elif(space_option == '3'):
        if (len(space.room) == 1):
            print("Co ty chcesz usunac?\nBrak adresow!\nNajpierw jakis dodaj!")
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
            update()
        elif(spaceDel == 0):
            certainly = input("Napewno usunac wszystkie adresy? y/n")
            if (certainly == 'y'):
                for index in range(1, len(space.room)):
                    del space.room[1]
                    update()
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
    if (len(space.room) == 1):
        print("Co ty chcesz zobaczyć?\nBrak adresow i notatek!")
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
    decorations.menu_rooms(False)
    num_where_add = input("do jakiego adresu przypisac notatke? ")
    
    if(testing(num_where_add)):
        num_where_add = int(num_where_add)
    else:
        print("Nie ma takiego adresu!")
        return

    content = input("Podaj tresc notatki: ")
    result = term()
    if (result == False):
        pass
    else:
        if(num_where_add in range(1, len(space.room))):
            content = content + " |term: " + result
            space.room[num_where_add].append(content)
            if(len(space.room[num_where_add]) > 3):
                sortek(num_where_add)
            update()
        else:
            print("Taki pokoj nie istnieje!")



                                #   Delete note    #
def delete():
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
            return
        
        if (num in range(1,len(space.room[delRoom]))):
            del space.room[delRoom][num]
            update()
            print("usunieto pomyslnie ;)")
            
        elif(num == 0):
            certainly = input("Napewno usunac wszystkie notatki? y/n")
            if(certainly == 'y'):
                for index in range(1, len(space.room[delRoom])):
                    del space.room[delRoom][1]
                    update()
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
