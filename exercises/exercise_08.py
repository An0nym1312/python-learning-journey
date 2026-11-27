print("Server Access Control")
benutzer = input("Bitte gib den Benutzernamen ein: ")
passwd = input("Bitte gib das Passwort ein: ")
stat = input("Bitte gib den Status des Kontos ein (aktiv o. gesperrt): ")

if not (stat  == "aktiv"):
    print("Benutzerkonto nicht aktiv")

elif (benutzer == "Admin" or benutzer == "Techniker") and passwd == "Python123":
    print("Zugang gewährt")

else:
    print("Keine Zugangsgenehmigung")

print("SAC abgeschlossen")
