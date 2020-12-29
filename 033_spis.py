slownikImie = {}
slownikNazwisko = {}
slownikWiek = {}

def dodajDoSlownika(klucz, rekord, slownik):
    if klucz in slownik:
        slownik[klucz].append(rekord)
    else:
        slownik[klucz] = [rekord]

def dodajDoSlownikow(rekord):
    dodajDoSlownika(rekord[0], rekord, slownikImie)
    dodajDoSlownika(rekord[1], rekord, slownikNazwisko)
    dodajDoSlownika(rekord[2], rekord, slownikWiek)

def dodajDane(dane):
    tab = dane.split(" ")
    imie = tab[0]
    nazwisko = tab[1]
    wiek = int(tab[2])
    rekord = (imie, nazwisko, wiek)
    dodajDoSlownikow(rekord)

def wyswietlPosortowane(slownik):
    for i in sorted(slownik.keys()):
        dane = slownik[i]
        for d in dane:
            print(d[0], d[1], d[2], sep=", ")

while True:
    dane = input("wprowadz dane (imie nazwisko wiek, x kończy wprowadzanie): ")
    if dane.lower() == 'x':
        print("Do zobaczenia!")
        break
    dodajDane(dane)

sortowanie = input("jak posorotwać dane? 1 - imie, 2 - nazwisko, 3 - wiek: ")
if sortowanie == "1":
    wyswietlPosortowane(slownikImie)
if sortowanie == "2":
    wyswietlPosortowane(slownikNazwisko)
if sortowanie == "3":
    wyswietlPosortowane(slownikWiek)