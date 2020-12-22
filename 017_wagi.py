print("""==========
Prosty kalkulator wagi
prosze podać miesiąc, dzień i wagę
operacja "x" kończy działanie programu
==========""")

wagi = [[0 for i in range(31)] for i in range(12)]

# zbieranie danych od użytkownika
while True:
    linia = input("podaj miesiac dzień i wagę (oddzielone spacjami): ") # 1 1 70
    if linia.lower() == "x":
        break
    
    lista = linia.split(" ")
    miesiac = int(lista[0]) - 1
    dzien = int(lista[1]) - 1
    waga = float(lista[2])
    # walidatory
    if miesiac < 0 or miesiac > 11:
        print("niepoprawny numer miesiąca (1-12)")
        continue
    if dzien < 0 or dzien > 30:
        print("niepoprawny dzień miesiąca (1-31)")
        continue
    if waga < 3 or waga > 300:
        print("niepoprawna waga (3-300)")
        continue
    wagi[miesiac][dzien] = waga

# operacje na danych
sumaRok, ileRok, maxRok, minRok = 0, 0, 0, 999
for i in range(len(wagi)):
    miesiac = wagi[i]
    sumaMiesiac, ileMiesiac, maxMiesiac, minMiesiac = 0, 0, 0, 999
    for dzien in miesiac:
        sumaMiesiac += dzien
        sumaRok += dzien
        if dzien != 0:
            ileMiesiac += 1
            ileRok += 1
            if maxMiesiac < dzien:
                maxMiesiac = dzien
            if minMiesiac > dzien:
                minMiesiac = dzien
            if maxRok < dzien:
                maxRok = dzien
            if minRok > dzien:
                minRok = dzien
    if ileMiesiac == 0:
        print("brak danych dla miesiąca:", i + 1)
    else:
        print("miesiąc " + str(i + 1) \
            + " - średnia waga: " + str(round(sumaMiesiac / ileMiesiac, 2)) \
            + ", maksymalna waga: " + str(maxMiesiac)\
            + ", minimalna waga: " + str(maxMiesiac))
        
if ileRok == 0:
    print("brak danych do wyliczeń")
else:
    print("rok" \
        + " - średnia waga: " + str(round(sumaRok / ileRok, 2)) \
        + ", maksymalna waga: " + str(maxRok)\
        + ", minimalna waga: " + str(minRok))
