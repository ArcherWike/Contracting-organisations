import space
#############- Decoration and display functions -#########################

def ui():
    print("="*50)

def operations():
    ui()
    menu = [
        'Edytuj notatki',
        'Notatki',
        'Edytuj adresy',
        'Adresy',
        'Wyjdz'
    ]
    for x, an in enumerate(menu):
        print("\t",x+1 , an)
    ui()

def menu_rooms(do):
    ui()
    for x, an in enumerate(space.room[0:len(space.room)]):
        if(do):
            print("\t", x, an[0])
        elif(do == False):
            if (len(space.room) == 1):
                print("Brak adresow!")
                return
            if(x == 0):
                pass
            else:
                print("\t", x, an[0])

    ui()


def rooms_option():
    ui()
    space_menu = [
        'zobacz miejsca',
        'dodaj adres',
        'usun adres'
    ]

    for x, an in enumerate(space_menu):
        print("\t",x+1, an)
    ui()




def see_menu():
    ui()
    print("|\t\t\tMENU\t\t\t|")
    ui()


def display_notes(index):
    for y in range(1, len(space.room[index])):
        print('\t', y, (space.room[index][y]))
