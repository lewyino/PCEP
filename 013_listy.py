lista = [1, 2, 3, 4]
print(lista) # [1, 2, 3, 4]
print(lista[0]) # 1

print("długość listy:", len(lista)) # długość listy: 4
del lista[1]
print("nowa długość listy:", len(lista)) # nowa długość listy: 3

lista[2] = 5
print(lista) # [1, 3, 5]

lista.append(7)
print(lista) # [1, 3, 5, 7]

lista.insert(2, 4)
print(lista) # [1, 3, 4, 5, 7]

lista[5] = 9 # error
