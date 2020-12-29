from operator import itemgetter

spis = []

def dodajDane(dane):
    tab = dane.split(" ")
    imie = tab[0]
    nazwisko = tab[1]
    wiek = int(tab[2])
    rekord = (imie, nazwisko, wiek)
    spis.append(rekord)

def wyswietlPosortowane(itemNumber):
    spis.sort(key=itemgetter(itemNumber))
    for d in spis:
            print(d[0], d[1], d[2], sep=", ")

while True:
    dane = input("wprowadz dane (imie nazwisko wiek, x kończy wprowadzanie): ")
    if dane.lower() == 'x':
        print("Do zobaczenia!")
        break
    dodajDane(dane)

sortowanie = input("jak posorotwać dane? 1 - imie, 2 - nazwisko, 3 - wiek: ")
if sortowanie == "1":
    wyswietlPosortowane(0)
if sortowanie == "2":
    wyswietlPosortowane(1)
if sortowanie == "3":
    wyswietlPosortowane(2)