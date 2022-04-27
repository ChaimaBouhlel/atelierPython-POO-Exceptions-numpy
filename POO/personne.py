#début définition
class Personne:
    """Classe Personne"""

    profession = "Njara"

    #constructeur
    def __init__(self):
        #lister les champs
        self.nom = ""
        self.__age = 0
        self.salaire = 0.0

    #fin constructeur

    def saisie(self,nom,age,salaire):
        self.nom=nom
        self.__age=age
        self.salaire=salaire

    def affiche(self):
        print("{Nom:",self.nom+", Age: "+str(self.__age)+", Salaire: "+str(self.salaire)+"}")

    @staticmethod
    def changerProfession(profession):
        Personne.profession = profession
        print("la profession devient: "+Personne.profession)


#fin définition

p1 = Personne()
nom = input("Donner nom ")
age = input("Donner Age ")
salaire = input("Donner Salaire ")
p1.saisie(nom, age, salaire)
p1.__age = 20
p1.affiche()
print(p1.__age)
print(p1._Personne__age)
p1._Personne__age=70
p1.affiche()
print(dir(p1))
print(isinstance(p1,Personne))
p1.changerProfession("Medecine")
Personne.changerProfession("Génie Logicielle")
