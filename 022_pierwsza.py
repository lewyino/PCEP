def pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

print("\"x\" kończy działanie programu")
while True:
    znak = input("Sprawdź czy liczba jest pierwsza: ")
    if znak.lower() == "x":
        break
    liczba = int(znak)
    print(pierwsza(liczba))