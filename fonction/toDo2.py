from fonction.appel_api import  appel_data_byId

import datetime


def verification(age, intervall1, intervall2):
    if intervall1 <= age < intervall2:
        return True
    return False


def egalite_tranche(tab1, tab2):
    if tab1[0] == tab2[0]:
        return True
    return False


def todo_2(donnee, type_data):
    tabTranche = []
    tranche = int(input("Choissisez la tranche d'age: "))
    for i in range(15, 90, tranche):
        tabTranche.append(i)

    for i in range(0, len(tabTranche) - 1):
        globals()['Tab_{}-{}'.format(str(tabTranche[i]), str(tabTranche[i + 1]))] = []
        for elementTab in donnee['data']:
            full = appel_data_byId(type_data, elementTab["id"])
            taona = datetime.datetime.now().year - int(full["dateOfBirth"].split("-", 1)[0])
            if verification(taona, tabTranche[i], tabTranche[i + 1] - 1):
                globals()['Tab_{}-{}'.format(str(tabTranche[i]), str(tabTranche[i + 1]))].append([taona, full["title"], full["firstName"], full["lastName"]])
        taille = len(globals()['Tab_{}-{}'.format(str(tabTranche[i]), str(tabTranche[i + 1]))])
        if taille !=0:
             print('Nombre de personne agee entre {}-{}ans: {}'.format(tabTranche[i],tabTranche[i + 1]-1, taille))
             for el1 in globals()['Tab_{}-{}'.format(str(tabTranche[i]), str(tabTranche[i + 1]))]:
                    print("{} {} {}".format(el1[1], el1[3], el1[2]))   
    
