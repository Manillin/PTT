class Materia:
    def __init__(self,n_materia,t_totale):
        self.n_materia=n_materia
        self.t_totale=t_totale

    def add_time(self,extra_time):
        self.t_totale += extra_time
    
    def get_time(self):
        return self.t_totale
    

    def get_time_ms(self):
        return f"{self.t_totale//60}h {self.t_totale%60}m"
    
    def get_n_materia(self):
        return self.n_materia
    
