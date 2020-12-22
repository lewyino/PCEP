a = float(input("Podaj długość pierwszej przyprostokątnej: "))
b = float(input("Podaj długość drugiej przyprostokątnej: "))

# a^2 + b^2 = c^2
c = (a**2 + b**2) ** 0.5
print("dla przyprostokątnych a=", a, ", b=", b, ", przeciwprostokątna=", c, sep="")