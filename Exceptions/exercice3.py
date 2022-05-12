somme = 0
for i in range(5):
    try:
        note = float(input("Entrer la note: "))
        if note < 0 or note > 20:
            raise ValueError
        else:
            somme += note
    except ValueError:
        print("Note non valide, la note doit être un réel entre 0 et 20")
        break
    except Exception as e:
        print("erreur de type", type(e))

if i==4:
    print(somme / 5)
