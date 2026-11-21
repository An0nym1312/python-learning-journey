print("IT Kostenrechner")

server = float(input("Wieviel kostet der Server?\n"))
ssd = float(input("Wieviel kostet die SSD?\n"))
budget = 500

gesamt = server + ssd
rest = budget - gesamt
durch = gesamt / 2


print("Im Durchsnitt kosten Server und SSD", durch, "€")
print("Die gesamtkosten belaufen sich auf", gesamt, "€")
print("Von deinem Budget von", budget, "€ hast du noch", rest, "€ übrig")
print(type(gesamt))