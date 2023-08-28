from materia_class import Materia
import pickle


class MatHolder:
    
    def __init__(self):
        self.lista_materie = []
        self.somma_tot = 0
        self.daily_tot = 0

    def add_materia(self,materia:Materia):
        self.lista_materie.append(materia)
        self.somma_tot += materia.get_time()

    def get_materia_by_string(self, target):
        materia: Materia
        for materia in self.lista_materie:
            if materia.get_n_materia().lower() == target.lower():
                return materia 
        return None
    
    def print_materie(self):
        materia: Materia 
        for materia in self.lista_materie:
            print(f"{materia.get_n_materia} -> {self.minuti_to_secondi(materia.get_time())}",end='\n')

    def minuti_to_secondi(self,minuti):
        return f"{minuti//60}h {minuti%60}m"
    

    def salva_su_file(self,file_name):
        with open(file_name,"wb") as f:
            pickle.dump(self.lista_materie,f)
        print("Scrittura completata")


    def carica_da_file(self,file_name):
        try:
            with open(file_name,"rb") as f:
                self.lista_materie=pickle.load(f)
        except (IOError, pickle.UnpicklingError):
            print("Eccezione nel caricamento da file...")
            return False
        return True
    
    def load(self):
        self.carica_da_file("/Users/chris/TechWeb/CTT/progresso.pkl")
