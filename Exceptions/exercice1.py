valid = False
while not valid:
    user_input = input("Donner un nombre positif: ")
    try:
        number = int (user_input)
        if (number < 0):
            raise ValueError()
        valid = True
    except ValueError:
        print("Il faut saisir un nombre positif")
    except Exception as exc:
        print("erreur de type:", type(exc))
print(" la racine de ", number,": ", number**0.5)
