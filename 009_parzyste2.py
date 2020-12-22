x = int(input("podaj liczbę całkowitą większą od 0: "))

if x < 1:
    exit(1)

counter = 0
for i in range(2, x + 1, 2):
    print(i)
    counter += 1

print("liczb parzystych większych od 0 i nie większych od", x, "jest: ", counter)
