x = int(input("podaj liczbę całkowitą większą od 0: "))

if x < 1:
    print("podana liczba nie jest większa od 0")
    exit(1)

counter = 0
i = 2
while i <= x:
    print(i)
    counter += 1
    i += 2
    # alternatywnie
    # if i % 2 == 0:
    #     print(i)
    #     counter += 1
    # i += 1

print("liczb parzystych większych od 0 i nie większych od", x, "jest: ", counter)
