courses = []
while True:
    article = input("Article à ajouter (tapez 'fin' pour terminer) : ")
    if article == 'fin':
        break
    courses.append(article)

with open("liste_courses.txt", "w") as f:
    for item in courses:
        f.write(item + "\n")
print("Liste de courses sauvegardée dans liste_courses.txt")