print("Server Maintenance Control")

svrname = input("Bitte gib den Server Namen ein: ")
user = input("Bitte gib deinen Benutzernamen ein: ")
passwd = input("Bitte gib dein Password ein: ")
wartung = input("Wartungsmodus aktiv o. inaktiv? ")

print("Servername: ", svrname)
print("Benutzer: ", user)
print("Wartungsstatus: ", wartung)

if user == "Admin" and passwd == "Python123":

    if not (wartung == "inaktiv"):
        print("Wartung ist genehmigt")

    else:
        print("Wartungsmodus inaktiv")

else:
    print("Keine Berechtigung für diese Aktion")

print("Server Maintenance Control abgeschlossen")
    
