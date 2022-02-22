import decorations
import space



def update():
    file = open('address.txt', 'w')
    file.writelines(str(space.room))
    file.close()

#--------------------------#   Input testing   #-------------------------------#

                #----------testing function----------
            #   checks the input if it is of type int
            #   returns True
            #   otherwise returns False
def testing(x):
    for num in range(0, len(space.room)):
        if(x == str(num)):
            return True
    return False


                        #check_term
                    #to the function below
        #asks whether the user wants to enter the date again or exit
def check_term():
    certainly = input("Czy chcesz sprobowac ponownie? y/n")
    if (certainly == 'y'):
        return True
    elif (certainly == 'n'):
        return False



    #asks for a term
    #and checks the input if the user has entered a correct date
    #returns correct date   if It's not correct:
    #                               it calls check_term()
    #                                     if it wants to enter the date again, it calls itself, otherwise it exits
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
                        if(check_term() == True):
                            term()
                        else:
                            return False
                else:
                    print("Zly miesiac!")
                    if (check_term() == True):
                        term()
                    else:
                        return False
            else:
                print("Zly rok!")
                if (check_term() == True):
                    term()
                else:
                    return False
        else:
            print("Zla data! ")
            if (check_term() == True):
                term()
            else:
                return False
    else:
        print("Zla data! ")
        if (check_term() == True):
            term()
        else:
            return False


#------------------------------- GENERAL FUNCTION ------------------------------#

                        #__sorting function
def sortek(index):
    if (len(space.room[index]) == 1):
        return
    else:
        for z in range(2, len(space.room[index])*2):
            for y in range(2, len(space.room[index])):

                second_term = space.room[index][y].split(" |term: ")
                first_term = space.room[index][y - 1].split(" |term: ")

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



#############################################################################################
#                               VARIABLE  DOCUMENTATION                                     #
#############################################################################################
#   adrs   <- variable of list operation
#   $specifies the index of the room on which the operation is to be performed
#   $specified by the user in the following functions
#   $must be of type <int> (tested in the testing function)


#   numno   <- variable of list operation
#   $specifies the index of the note on which the operation is to be performed
#   $specified by the user in the functions below
#   $must be of type int (tested in the testing function)


#   content <-content variable to be added (note)
#   $contains the content of the note
#   $specified by the user in the functions below
#   $ <str> type


#   certainly <- confirm for sure variable
#   $protection of the user's inadvertent non-thinking
#   $specified by the user in the functions below
#   $confirmation only: 'y' (Yes) performs further functions
#   <str> type




###############################################################################################
###############################################################################################
#                           NOTE FUNCTIONS
###############################################################################################
###########
###########     1.Display/ 2.Add / 3.Delete
###########
###############################################################################################





                                #  1. Display note   #
def display():
    if (len(space.room) == 1):
        print("Co ty chcesz zobaczyć?\nBrak adresow i notatek!")
        return

    decorations.menu_rooms(True)
    adrs = input("zadania z ktorego adresu chcesz zobaczyc? ")

    if(testing(num)):
        adrs = int(adrs)
    else:
        print("Nie ma takiego adresu!")
        return

    if (adrs in range(1,len(space.room))):
        print("Adres " + str(space.room[adrs][0].capitalize()) + ": ")
        if(len(space.room[adrs]) > 1):
            decorations.display_notes(adrs)
        else:
            print("\n\t<Brak notatek>")
    elif(adrs == 0):
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
    



                                #  2. Add note   #

def add():
    decorations.menu_rooms(False)
    adrs = input("do jakiego adresu przypisac notatke? ")
    
    if(testing(adrs)):
        adrs = int(adrs)
    else:
        print("Nie ma takiego adresu!")
        return

    content = input("Podaj tresc notatki: ")


    teq(True)
    want_term = print("Czy chcesz dodac termin wykonania? ")

    if(want_term == '1'):
        pass
    elif(want_term == '2'):
        print("Nie ma jeszcze niedodawania xD Musisz dodać :P")
    elif(want_term == '3'):
        print("Mozesz dodac termin wykonania, w ktorym masz wykonac notatke\nPomoze Ci to w organizacji zadan\n Zobaczysz na ktore zadanie masz malo czasu, bo są sortowane w kolejności terminu na wykonanie zadania")
        teq(False)
        want_term = print("Czy chcesz dodac termin wykonania? ")
        if (want_term == '1'):
            print('Nie ma jeszcze niedodawania xD Musisz dodać :P')
        elif (want_term == '2'):
            return
    else:
        print("Nie ma takiego wyboru!")

    result = term()
    if (result == False):
        pass
    else:
        if(adrs in range(1, len(space.room))):
            content = content + " |term: " + result
            space.room[adrs].append(content)
            if(len(space.room[adrs]) > 3):
                sortek(adrs)
            update()
        else:
            print("Taki pokoj nie istnieje!")



                                #  3. Delete note    #
def delete():
    decorations.menu_rooms(True)
    
    adrs = input("Z jakiego pokoju usunac notatke? ")
    if(testing(adrs)):
        adrs = int(adrs)
    else:
        print("Nie ma takiego pokoju!")
        return
        

    if (adrs in range(1, len(space.room))):
        print("Pomieszczenie " + str(space.room[adrs][0])+'\n')
        if (len(space.room[adrs]) < 2):
            print("Brak notatek!")
            return
        else:
            print("\t 0 Usun wszystkie")

        decorations.display_notes(adrs)
        
        numno = input("Jaki numer ma notatka do usuniecia? ")
  
        if(testing(numno)):
            numno = int(numno)
        else:
            print("nie ma takiej notatki!")
            return
        
        if (numno in range(1,len(space.room[adrs]))):
            del space.room[adrs][numno]
            update()
            print("usunieto pomyslnie ;)")

        elif(numno == 0):
            certainly = input("Napewno usunac wszystkie notatki? y/n")
            if(certainly == 'y'):
                for index in range(1, len(space.room[adrs])):
                    del space.room[adrs][1]
                    update()
            elif(certainly == 'n'):
                return
            else:
                print("Nie ma takiego wyboru!")
        else:
            print("Nie ma takiego wyboru!")
    elif(adrs == 0):
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
