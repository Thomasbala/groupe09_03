phrase = input("Entrez une phrase : ")
nb_mots = len(phrase.split())
nb_caracteres = len(phrase)

report_content = f"Analyse de texte :\n" \
                 f"Phrase : {phrase}\n" \
                 f"Nombre de mots : {nb_mots}\n" \
                 f"Nombre de caractères : {nb_caracteres}\n"

with open("rapport_analyse_texte.txt", "w") as f:
    f.write(report_content)
print("Rapport d'analyse de texte sauvegardé dans rapport_analyse_texte.txt")