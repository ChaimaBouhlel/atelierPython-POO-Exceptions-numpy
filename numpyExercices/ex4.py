import numpy as np

tabInitial = np.arange(10,34).reshape(8,3)
print("tableau initial")
print(tabInitial)
print()
print("On divise ce tableau en quatre sous-tableaux de taille égale")
for i in range(0,8,2):
    sstab = np.array([])
    sstab= np.append(sstab,tabInitial[i:i+2]).reshape(2,3)
    print("sous-tableau numéro",int((i+2)/2))
    print(sstab)

