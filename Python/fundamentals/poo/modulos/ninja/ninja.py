<<<<<<< HEAD
from Mascota import Mascota

class ninja():
    def __init__(self, nombre, apellido, premios, comida_Mascota, Mascota):
        self.nonbre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_Mascota = comida_Mascota
        self.Mascota = Mascota

    def caminar(cls,self):
        self,Mascota.jugar()
        return self
        

    def alimentar(self):
        if len(self.comida_Mascota) > 0:
            food = self.comida_Mascota.pop()
            print(f"alimentar {self.Mascota.nombre} {comida}!")
            self,Mascota,comida()
        else:
            print("o no nesecitas mas comida Mascota")
        return self
        
    def bañar(self):
        self,Mascota.sonido()
        mis_golosinas = ['jamon, carne']
        mi_comida = ['pizza, burger']
=======
from mascota import Mascota

class Ninja:
    def __init__(self, nombre, apellido, premio, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.comida_mascota = comida_mascota
        self.mascota = mascota
    
    def caminar(self):
        self.mascota.jugar()
    
    def alimentar(self):
        self.mascota.comer()
    
    def bañar(self):
        self.mascota.sonido()
>>>>>>> 4df5c425a2022e3c17fc5709bce2736c4a3ed089
