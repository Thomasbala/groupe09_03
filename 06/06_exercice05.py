n = int(input("Entrez un entier positif: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print(f"La factorielle de {n} est {fact}")