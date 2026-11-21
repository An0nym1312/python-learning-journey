# Das ist ein Kommentar

print("Hallo Welt")

name = input("Wie heißt du?\n")
beruf = input("Was möchtest du irgendwann mal werden?\n")
alter = int(input("Wie alt bist du aktuell?\n"))

print("============================================")
print("=== Steckbrief ===============", name, "====")
print("============================================")
print("Dein Wunschberuf:", beruf)
alter = alter + 10
print("Dein Alter in 10 Jahren ist:", alter)
print(type(alter))