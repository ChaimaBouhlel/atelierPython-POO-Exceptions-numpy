class Compte:
    def __init__(self, id, debit=0, credit=0):
        self.debit = debit
        self.credit = credit
        self.id = id

    def affiche(self):
        print("{Compte-Id: " + str(self.id) + ", debit: " + str(self.debit) + ', credit: '+ str(self.credit)+"}")

    def ajout(self, montant):
        self.credit += montant

    def retire(self, montant):
        self.debit += montant

    def credit(self, montant):
        self.credit += montant

    def solde(self):
        return self.credit - self.debit


class CompteEpargne(Compte):
    def __init__(self, id, debit=0, credit=0, taux=0, nom="Personne"):
        super().__init__(id, debit, credit)
        self.taux = taux
        self.nom = nom

    def affiche(self):
        print("Compte epargne de:", self.nom)
        print("     id:", self.id)
        print("     débit:", self.debit)
        print("     taux:", self.taux)

    def interet(self):
        return self.solde() * self.taux

    def update(self):
        self.credit += self.interet()


c = Compte(122,500,400)
c.affiche()
print("On retire 200 dt")
c.retire(200)
c.affiche()
print("Le solde devient: "+str(c.solde()))
print("On ajoute 800dt")
c.ajout(800)
print("Le solde devient: "+str(c.solde()))
print("Deuxième affichage:")
c.affiche()
print()

ce = CompteEpargne(123, 1000, 2000, 0.1, "Edam")
ce.affiche()
print("On retire 200 dt")
ce.retire(200)
ce.affiche()
print("Le solde devient: "+str(ce.solde()))
print("On ajoute 800dt")
ce.ajout(800)
print("Le solde devient: "+str(ce.solde()))
print("Interet:"+str(ce.interet()))
print("On fait un update")
ce.update()
print("Deuxième affichage:")
ce.affiche()