# Programme qui calcule et affiche la somme d'une suite
n=int(input("Veuillez entrer un entier : "))
s=0
for i in range(1,n+1):
    s=s+1.0/i
print(f"La somme est {s}")
