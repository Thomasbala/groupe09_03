nom_etudiant = input("Nom de l'étudiant : ")
note1 = float(input("Note 1 (sur 20) : "))
note2 = float(input("Note 2 (sur 20) : "))
note3 = float(input("Note 3 (sur 20) : "))

moyenne = (note1 + note2 + note3) / 3

with open("notes_etudiants.txt", "a") as f:
    f.write(f"Étudiant: {nom_etudiant}, Notes: {note1}, {note2}, {note3}, Moyenne: {moyenne:.2f}\n")
print("Notes de l'étudiant sauvegardées dans notes_etudiants.txt")