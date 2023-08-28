from materia_class import Materia 
from materiaHolder import MatHolder

import pickle


def salva_su_file(file_name,lista_materie):
    with open(file_name,"wb") as f:
        pickle.dump(lista_materie,f)
    print("Scrittura completata")


def leggi(file_name):
    print("Lettura del file: ")
    try:
        with open(file_name,"rb") as f:
            lista_materie2 =pickle.load(f)
    except(IOError,pickle.UnpicklingError):
        print("Eccezione nel caricamento da file...")
        return []
    return lista_materie2




file_name = "/Users/chris/TechWeb/CTT/progresso.pkl"
lista_materie=[]
lista_materie2=[]
materia: Materia

materia = Materia("Sistemi Operativi",260)
lista_materie.append(materia)
for materia in lista_materie:
    print(materia.get_n_materia())
#salva_su_file(file_name,lista_materie)
lista_materie2 = leggi(file_name)
print("Lettura Lista 2: ")
for materia in lista_materie2:
    print(f"{materia.get_n_materia()} -> {materia.get_time()}")
