tajnaLiczba = 13

counter = 0
while True:
    liczba = int(input("Zgadnij jaką liczbę mam na myśli: "))
    if liczba == tajnaLiczba:
        print("BRAWO!!! zgadłeś liczbę którą miałem na myśli")
        break
    print("to nie ta liczba, próbuj dalej...")
    counter += 1
    if counter > 2:
        if liczba < tajnaLiczba:
            print("podpowiem Ci, ze tajna liczba jest większa ;)")
        else:
            print("podpowiem Ci, ze tajna liczba jest mniejsza ;)")