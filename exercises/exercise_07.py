print("_______________________________________")
print("S e r v e r  H e a l t h  M o n i t o r")
print("_______________________________________")

svrname = input("Bitte geben sie der Servernamen ein: ")
cpu = float(input("Bitte geben sie die CPU-Auslastung in Prozent an: "))
ram = float(input("Bitte geben sie die RAM-Auslastung in Prozent an: "))
cpu_temp = float(input("Bitte geben sie die CPU Teperatur in °C ein: "))
svrstat = input("Bitte geben sie den Status des Servers ein (offline o. online): ")
print()
print("Übersicht für ",svrname)
print("======================")

print("CPU Auslastung:", cpu)
print("RAM Auslastung;", ram)
print("CPU Temperatur: ", cpu_temp, "°C")
print("Serverstatus: ", svrstat)

if not (svrstat == "online"):
    print("Gesundheit nicht auswertbar, Server ist offline")

elif cpu >= 90 or ram >= 90 or cpu_temp >= 90:
    print("Gesundnheit des Servers: KRITISCH!")

elif (cpu >= 75 and ram >= 75) or cpu_temp >= 75:
    print("Gesundnheit des Servers: WARNUNG!")

else:
    print("Gesundnheit des Servers: GESUND")

print("Gesundheitsüberwachung erfolgreich abgeschlossen")