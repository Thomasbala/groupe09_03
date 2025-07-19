texte = input("Entrez un texte : ")
mot_a_chercher = input("Mot à chercher : ").lower()
compte = texte.lower().count(mot_a_chercher)
print(f"Le mot '{mot_a_chercher}' apparaît {compte} fois.")