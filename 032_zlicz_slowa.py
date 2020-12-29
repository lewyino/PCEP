slownik = {}

while True:
    slowa = input("wprowadz slowa: ")
    if slowa.lower() == 'x':
        print("Do zobaczenia!")
        break
    tab = slowa.split(" ")
    for slowo in tab:
        if slowo in slownik:
            slownik[slowo] += 1
        else:
            slownik[slowo] = 1
    
for slowo in sorted(slownik.keys()):
    print(slowo, ":", slownik[slowo])
