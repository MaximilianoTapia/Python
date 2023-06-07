class Mascota:
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
    
    def dormir(self):
        self.energia += 25
    
    def comer(self):
        self.energia += 5
        self.salud += 10
    
    def jugar(self):
        self.salud += 5
    
    def sonido(self):
        print("Sonido de la mascota")
