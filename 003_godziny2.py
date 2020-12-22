przelicznik = 60

godziny = float(input("Podaj liczbę godzin do zamiany na minuty: "))
minuty = godziny * przelicznik
print(godziny, "godziny to", int(minuty), "minuty")

minuty = int(input("Podaj liczbę minut do zamiany na godziny: "))
godziny = minuty / przelicznik
print(minuty, "minuty to", godziny, "godziny")
print(minuty, "minuty to", round(godziny, 2), "godziny")
