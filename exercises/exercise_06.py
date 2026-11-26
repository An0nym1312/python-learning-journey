print("Server Temprature Monitor")

svrname = input("Bitte geben sie den Servernamen ein: ")
temp = float(input("Bitte geben sie die Temperatur der CPU ein: "))

print("Server: ", svrname)
print("CPU Temperatur: ", temp, "°C")

if temp < 60:
    print("Abschlussmeldung: Temperatur normal")

elif temp < 75:
    print("Abschlussmeldung: Erhöhte Temperatur")

elif temp < 90:
    print("Abschlussmeldung: Hohe Temperatur")

else:
    print("Abschlussmeldung: Kritische Temperatur")

print("Temperaturüberwachung abgeschlossen")

