phrase = input("Entrez une phrase à ajouter au journal : ")
with open("journal.txt", "a") as f:
    f.write(phrase + "\n")
print("Phrase ajoutée au journal.txt")