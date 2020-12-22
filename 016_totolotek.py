wylosowane = [1, 11, 15, 23, 35, 47]

wybrane = []
for i in range(6):
    wybrane.append(int(input("\"Skreśl\" liczbę: ")))

trafione = []
for i in wybrane:
    if i in wylosowane:
        trafione.append(i)

print("trafiłeś", str(len(trafione)), "liczb:", str(trafione))
