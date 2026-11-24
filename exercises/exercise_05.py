print("=========================================")
print("S E R V E R  S T O R A G E  M O N I T O R")
print("=========================================")
print("\n")

print("Willkommen zu ihrem Server Storage Monitor")
srvname = input("Bitte geben sie ihren Servernamen ein: ")
ges = int(input("Bitte geben sie ihre Gesamtkapazität in GB ein: "))
bel = int(input("Bitte geben sie ihren Belegten Speicher in GB ein: "))
frei = ges - bel
proz = bel * 100 / ges 
print("\n")
print("----------Serverstatus----------")
print("Server: ", srvname)
print("Gesamtkapazität: ", ges)
print("Belegter Speicher: ", bel)
print("Freier Speicher: ", frei)
print("Speicherauslastung: ", proz, "%")
print("\n")
print("\n")

if proz >= 90:
    print("K R I T I S C H E  A U S L A S T U N G")

elif proz >= 75:
    print("W A R N U N G: Hohe Auslastung")

else:
    print("Normale Auslastung")

print("=======================================================")
print("Ü B E R W A C H U N G  A B G E S C H L O S S E N")
print("Bei Rückfragen wenden sie sich bitte an ihren Admin")