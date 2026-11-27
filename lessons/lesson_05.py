# Lesson 5 - Nested if

ausweis = True
berechtigung = True

if ausweis == True:
    print("Ausweis gültig")

    if berechtigung == True:
        print("Zugang gewährt")

    else:
        print("Berechtigung fehlt")

else:
    print("Ausweis ungültig")

print("Konrolle abgeschlossen")