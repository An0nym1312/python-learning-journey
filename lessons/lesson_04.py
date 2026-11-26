# Lesson 4 (Logische Operatoren)

# Logischer Operator: and

benutzername = input("Benutzername: ")
passwort = input("Passwort: ")

if benutzername == "admin" and passwort == "Python123":
    print("Zugriff erlaubt")

else:
    print("Zugriff verweigert")

# Logischer Operator: or

cpu = float(input("CPU-Auslastung in %: "))
ram = float(input("RAM-Auslastung in %: "))

if cpu >= 90 or ram >= 90:
    print("WARNUNG: Kritische Systemauslastung!")

else:
    print("Systemauslastung normal")

# Logischer Operator: not

server_online = True

if not server_online:
    print("WARNUNG: Server nicht erreichbar!")

else:
    print("Server ist erreichbar")

# Kombination logischer Operratoren

rolle = input("Benutzerrolle: ")
passwort = input("Passwort: ")

if (rolle == "Admin" or rolle == "Techniker") and passwort == "Python123":
    print("zugriff erlaubt")

else:
    print("Zugriff verweigert")
