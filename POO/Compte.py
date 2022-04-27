class Compte:
    def __init__(self, id, debit=0, credit=0):
        self.debit = debit
        self.credit = credit
        self.id = id

    def affiche(self):
        print("{Compte-Id: "+self.id+", debit: "+ self.debit + ", credit: ", self.credit )

    def retire(self, montant):
        self.debit += montant

    def credit(self, montant):
        self.credit += montant

    def solde(self):
        return self.credit-self.debit


"""class CompteEpargne(Compte):
    def __init__(self, taux=0, nom="Personne"):"""