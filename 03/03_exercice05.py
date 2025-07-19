# QUESTION 5
# ----------
mdp = input("Entrez un mot de passe: ")

has_digit = False
has_upper = False

for char in mdp:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if len(mdp) >= 8 and has_digit and has_upper:
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")