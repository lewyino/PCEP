znaki = [chr(i) for i in range(97, 123)]
znaki += [i.upper() for i in znaki]
znaki.append(" ")
print("obsługiwane znaki:", znaki)

def cezar(ciagZnakow, kod):
    wynik = ""
    for i in ciagZnakow:
        znak = 0
        for j in znaki:
            if i == j:
                wynik += znaki[(znak + kod) % len(znaki)] 
                znak = -1
                break
            if znak == -1:
                break
            znak += 1
    return wynik

haslo = input("Wprowadź ciąg znaków: ")
operacja = int(input("1 - zaszyfruj, 2 - odszyfruj: "))

kod = 3 if operacja == 1 else -3
wynik = cezar(haslo, kod)
print("wynik:", wynik)
