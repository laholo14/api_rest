from fonction.appel_api import appel_data
from fonction.appel_api import appel_data_byId

def todo_1(donnee,type_data):
    for elementTab in donnee['data']:
       farany = appel_data_byId(type_data,elementTab["id"])
       print("\n{} {} {}\n{}\n{}".format(elementTab["title"], elementTab["lastName"], elementTab["firstName"], elementTab["email"], farany["phone"]))

