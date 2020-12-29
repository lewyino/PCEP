import datetime

def przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        return True
    return False

def dniWMiesiacu(rok, miesiac):
    if miesiac == 2:
        if przestepny(rok):
            return 29
        return 28
    if miesiac > 7:
        return 31 if miesiac % 2 == 0 else 30
    return 30 if miesiac % 2 == 0 else 31

def dzienRoku(rok, miesiac, dzien):
    if miesiac > 12 or miesiac < 1:
        return None
    if dniWMiesiacu(rok, miesiac) < dzien or dzien < 1:
        return None
    dni = 0
    for i in range(1, miesiac):
        dni += dniWMiesiacu(rok, i)
    dni += dzien
    return dni

def podajDate():
    data = input("podaj date: ")
    tab = data.split("-")
    return (int(tab[0]), int(tab[1]), int(tab[2]))

def porownajDaty(data1, data2):
    return datetime.date(data1[0], data1[1], data1[2]) < datetime.date(data2[0], data2[1], data2[2])  

def liczNiedziele(start, koniec):
    suma = 0
    for i in range(1900, start[0]):
        suma += 366 if przestepny(i) else 365
    suma += dzienRoku(start[0], start[1], start[2]) - 6 - 1
    sumaKoniec = 0
    for i in range(1900, koniec[0]):
        sumaKoniec += 366 if przestepny(i) else 365
    sumaKoniec += dzienRoku(koniec[0], koniec[1], koniec[2]) - 6 - 1
    roznica = sumaKoniec - suma
    return roznica // 7

def liczNiedziele2(start, koniec):
    start = datetime.date(start[0], start[1], start[2])
    koniec = datetime.date(koniec[0], koniec[1], koniec[2])
    roznicaStartPierwszaNiedziela = (start - datetime.date(1900, 1, 7)).days
    roznicaKniecPierwszaNiedziela = (koniec - datetime.date(1900, 1, 7)).days
    roznica = roznicaKniecPierwszaNiedziela - roznicaStartPierwszaNiedziela
    return roznica // 7

start = podajDate()
koniec = podajDate()
if porownajDaty(start, koniec) == False:
    print("pierwsza data musi być mniejsza od drugiej")
else:
    print(liczNiedziele(start, koniec))
    print(liczNiedziele2(start, koniec))