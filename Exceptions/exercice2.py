def dire_bonjour_a(nom):
    try:
        if (type(nom)==str):
            print("Bonjour "+nom)
            if (nom ==''):
                raise ValueError("chaine vide")
        else:
            raise ValueError("c'est pas une chaine")
    except Exception as Exc:
        print("erreur de type: ",type(Exc))
        print(Exc)


user_input=input("Saisir le nom: ")
dire_bonjour_a(user_input)
dire_bonjour_a(23)
dire_bonjour_a(None)
