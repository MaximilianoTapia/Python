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
