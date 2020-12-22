a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a > b:
    print("pierwsza podana liczba jest większa")
elif a < b: # b > a
    print("druga podana liczba jest większa")
else:
    print("podane liczny są takie same")
