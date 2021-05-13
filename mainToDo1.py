from fonction.appel_api import appel_data
from fonction.input import entrer
from fonction.toDo1 import todo_1

entrer = entrer()


# print du todo_1
if entrer[0] == "user":

    try:
        data1 = appel_data(entrer[0],entrer[1])
        todo_1(data1,entrer[0])
    except:
        print(data1) 
      
else :
   print("Pas de sujet sur {}".format(entrer[0]))


