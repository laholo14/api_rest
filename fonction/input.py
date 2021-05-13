def entrer():
    limite = 0
    type_data = input("Entrer le type de donnee a afficher (user,location,tag,post ou comment): ")
    while limite < 5 or limite > 50:
        limite = int(input("Entrer limite de valeur 5 a 50 : "))
    
    return type_data,limite