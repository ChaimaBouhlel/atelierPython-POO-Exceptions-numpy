import numpy as np

tab = np.arange(100,350,10).reshape(5,5)
print("Voivi le tableau numPy initial:")
print(tab)
vecteur = np.array([])
for i in range(5):
    vecteur = np.append(vecteur,tab[i][2])

print()
print("un tableau d'éléments en prenant la troisième colonne de toutes les lignes")
print(vecteur)