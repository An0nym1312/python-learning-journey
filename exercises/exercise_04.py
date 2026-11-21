print("Hallo, Willkommen zu deinem Einnahmen und Ausgaben Tracker")
name = input("Wie heißt du?\n")
einkommen = float(input("Wie viel ist dein monatliches Einkommen?\n"))
fixkosten = float(input("Wie viel gibst du monatlich für Heizung, Miete, Versicherungen, etc aus?\n"))
freizeit = float(input("Wie viel gibst du monatlich für Freizeitaktivitäteten aus?\n"))
ausgaben = fixkosten + freizeit
rest = einkommen - ausgaben
sparbetr = rest * 12

print("Monatsübersicht")
print("für", name)
print("\n")
print("Einnahmen: ", einkommen, "€")
print("Fixkosten: ", fixkosten, "€")
print("Freizeit: ", freizeit, "€")
print("Ausgaben monatlich gesamt: ", ausgaben, "€")
print("Möglicher monatlicher Sparbetrag: ", rest, "€")
print("Nach einem Jahr angesparter Betrag: ", sparbetr, "€")
print("----------------------------------------------------")

print(type(sparbetr))