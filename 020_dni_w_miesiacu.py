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

print(dniWMiesiacu(2000, 4))
print(dniWMiesiacu(2004, 2))
print(dniWMiesiacu(1900, 2))
print(dniWMiesiacu(1987, 8))
