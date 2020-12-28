def silnia(liczba):
    if liczba == 0:
        return 1
    return liczba * silnia(liczba - 1)

print("\"x\" kończy działanie programu")
while True:
    znak = input("podaj liczbę: ")
    if znak.lower() == "x":
        break
    liczba = int(znak)
    print(str(liczba) + "! = " + str(silnia(liczba)))
