listaNumerow = { "tata": 123123123, "mama": 123234345}
print(listaNumerow)
print(len(listaNumerow))

listaNumerow["tata"] = 123456678
print(listaNumerow["tata"])

print("tata" in listaNumerow)
print("Tata" in listaNumerow)

listaNumerow["sisotra"] = 456321876
print(len(listaNumerow))

listaNumerow.update({"brat": 987654321, "ciocia": 987986543})
print(len(listaNumerow))

del listaNumerow["ciocia"]
print(len(listaNumerow))

numer = listaNumerow.popitem()
print(numer)
print(len(listaNumerow))

for k in listaNumerow.keys():
    print(k, "->", listaNumerow[k])

for k in sorted(listaNumerow.keys()):
    print(k, "->", listaNumerow[k])

for v in listaNumerow.values():
    print(v)

for k, v in listaNumerow.items():
    print(k, "->", v)
