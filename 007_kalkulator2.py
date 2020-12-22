a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
operacja = input("Jaką operację chcesz wykonać? (+, -, *, /, **): ")

if operacja == '+':
    print(str(a) + " + " + str(b) + " = " + str(a+b))
elif operacja == '-':
    print(str(a) + " - " + str(b) + " = " + str(a-b))
elif operacja == '*':
    print(str(a) + " * " + str(b) + " = " + str(a*b))
elif operacja == '/':
    if b != 0:
        print(str(a) + " / " + str(b) + " = " + str(a/b))
    else:
        print("dzielenie przez 0 jest niedozwolone")
elif operacja == '**':
    print(str(a) + " ** " + str(b) + " = " + str(a**b))
else:
    print("nie umiem wykonać operacji \"" + operacja + "\" :(")
