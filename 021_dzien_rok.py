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

print(dzienRoku(2000, 1, 1))
print(dzienRoku(2021, 9, 13))
print(dzienRoku(1987, 3, 1))
print(dzienRoku(2000, 3, 1))
print(dzienRoku(2000, 13, 1))
print(dzienRoku(2000, 2, 29))
print(dzienRoku(2001, 2, 29))
