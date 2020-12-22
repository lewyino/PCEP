print("""==========
Prosty kalkulator
podaj typ operacji jaką chcesz wykonać
dozwolone operacje: + - * / ** max min
operacja "x" kończy działanie programu
następnie dodawaj liczby dla których chcesz dokonać obliczeń
==========""")

def suma(liczby):
    result = 0
    for i in liczby:
        result += i
    return result

def roznica(liczby):
    result = 0
    for i in liczby:
        result -= i
    return result

def iloraz(liczby):
    result = 1
    for i in liczby:
        result *= i
    return result

def iloczyn(liczby):
    result = liczby[0]
    for i in range(1, len(liczby)):
        result /= liczby[i]
    return result

def potega(liczby):
    result = liczby[0]
    for i in range(1, len(liczby)):
        result **= liczby[i]
    return result

def oblicz(operacja, liczby):
    if operacja == '+':
        print("suma liczb w zbiorze " + str(liczby) + ": " + str(suma(liczby)))
    elif operacja == '-':
        print("róznica liczb w zbiorze " + str(liczby) + ": " + str(roznica(liczby)))
    elif operacja == '*':
        print("iloraz liczb w zbiorze " + str(liczby) + ": " + str(iloraz(liczby)))
    elif operacja == '/':
        print("iloczyn liczb w zbiorze " + str(liczby) + ": " + str(iloczyn(liczby)))
    elif operacja == '**':
        print("potęga liczb w zbiorze " + str(liczby) + ": " + str(potega(liczby)))
    elif operacja == 'max':
        print("największa liczba w zbiorze " + str(liczby) + ": " + str(max(liczby)))
    elif operacja == 'min':
        print("najmniejsza liczba w zbiorze " + str(liczby) + ": " + str(min(liczby)))
    else:
        print("nie umiem wykonać operacji \"" + operacja + "\" :(")

while True:
    operacja = input("Jaką operację chcesz wykonać? (+, -, *, /, **, min, max, x): ")
    if operacja.lower() == 'x':
        print("Do zobaczenia!")
        break
    liczby = []
    while True:
        x = input("Podaj liczbę (x, kończy wprowadzanie liczb): ")
        if x.lower() == 'x':
            break
        liczby.append(float(x))

    oblicz(operacja, liczby)
