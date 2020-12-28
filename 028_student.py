oceny = {}

def sredniaUczen(imie):
    if imie not in oceny:
        print("Uczeń", imie, "nie ma ocen")
    else:
        suma = 0
        for ocena in oceny[imie]:
            suma += ocena
        srednia = suma / len(oceny[imie])
        print("Średnia dla ucznia", imie, "to:", srednia)

def sredniaUczniow(oceny):
    for imie in oceny:
        sredniaUczen(imie)

def srednia(oceny):
    suma = 0
    iloscOcen = 0
    for imie in oceny:
        for ocena in oceny[imie]:
            suma += ocena
            iloscOcen += 1
    srednia = suma / iloscOcen
    print("Średnia ocen wszystkich uczniów to:", srednia)

while True:
    imie = input("Podaj imię studenta: ")
    if imie.lower() == 'x':
        print("Czas na statystyki!")
        break
    ocena = float(input("Podaj ocenę: "))

    if imie in oceny:
        oceny[imie].append(ocena)
    else:
        oceny[imie] = [ocena]

srednia(oceny)
sredniaUczniow(oceny)
sredniaUczen("Zbigniew")