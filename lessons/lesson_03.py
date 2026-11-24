# Lesson 3 (Vergleichoperatoren und Bedingungen)

# Vergleichsoperatoren

print(10 == 10) # gleich
print(10 != 5) # ungleich
print(10 > 5) # größer
print(10 < 5) # kleiner
print(10 >= 10) # größer gleich 
print(10 <= 5) # kleiner gleich

# erste if-Bedingung

alter = int(input("Wie alt bist du? "))

if alter >= 18:
    print("Volljährig")

print("Programm beendet")

# if und else

alter = int(input("Wie alt bist du? "))

if alter >= 18:
    print("Du bist volljährig")
else:
    print("Du bist minderjährig")

# if, else und elif

cpu = int(input("Wie hoch ist deine CPU Auslastung? "))

if cpu >= 90:
    print("Kritische Auslastung")
elif cpu >= 70:
    print("Hohe Auslastung")
else:
    print("Normale Auslastung")