import random

punkty_komputer = 0
punkty_gracz = 0

while punkty_komputer != 3 or punkty_gracz != 3:
    #wybór komputera
    wybor_komputer_lista = ["Papier", "Kamień", "Nożyce"]
    wybor_komputer = random.choice(wybor_komputer_lista)

    #wybór gracza
    wybor_gracza = int(input("Co wybierasz?: \n 1 - Papier \n 2 - Kamień \n 3 - Nożyce\n :"))
    #  wybranie papieru przez gracza
    if wybor_gracza == 1:
        print("Wybrałeś papier")
        if wybor_komputer == "Papier":
            print("Komputer wybrał papier")
            print("Remis!")
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))

        if wybor_komputer == "Kamień":
            print("Komputer wybrał kamień")
            print("Wygrałeś :>")
            punkty_gracz += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))
    
        if wybor_komputer == "Nożyce":
            print("Komputer wybrał nożyce")
            print("Przegrałeś :<")
            punkty_komputer += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))

    #wybranie kamienia przez gracza
    elif wybor_gracza == 2:
        print("Wybrałeś kamień")
        if wybor_komputer == "Papier":
            print("Komputer wybrał papier")
            print("Przegrałeś :<")
            punkty_komputer += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))

        if wybor_komputer == "Kamień":
            print("Komputer wybrał kamień")
            print("Remis!")
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))
    
        if wybor_komputer == "Nożyce":
            print("Komputer wybrał nożyce")
            print("Wygrałeś :>")
            punkty_gracz += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))

    #wybranie nożyc przez gracza
    elif wybor_gracza == 3:
        print("Wybrałeś nożyce")
        if wybor_komputer == "Papier":
            print("Komputer wybrał papier")
            print("Wygrałeś :>")
            punkty_gracz += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))

        if wybor_komputer == "Kamień":
            print("Komputer wybrał kamień")
            print("Przegrałeś :<")
            punkty_komputer += 1
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))
    
        if wybor_komputer == "Nożyce":
            print("Komputer wybrał nożyce")
            print("Remis!")
            print("Punkty gracza: " + str(punkty_gracz))
            print("Punkty komputera: " + str(punkty_komputer))
    else:
        print("Nie ma takiej opcji")
        continue
    if punkty_komputer == 3:
        print("Komputer z tobą wygrał :<")
        break
    elif punkty_gracz == 3:
        print("Wygrałeś z komputerem :>")
        break