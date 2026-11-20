print("Willkommen zu deinem Python Taschenrechner")

zahl1 = int(input("Bitte gib die erste zahl ein: "))
zahl2 = int(input("Bitte gib die zweite Zahl ein: "))

add = zahl1 + zahl2
sub = zahl1 - zahl2
mul = zahl1 * zahl2
div = zahl1 / zahl2

print("Addition: ", add)
print("Subtraktion: ", sub)
print("Multiplikation: ", mul)
print("Division: ", div)

print("Datentyp der Divison: ", type(div))