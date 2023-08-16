
class Mascota:
    def __init__(self,name, tipo, golosinas, salud, energia):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 50
    def dormir(self):
        self.energia +=25
        return self
        pass
    def comer(self):
        self.energia +=5
        self.salud +=10
        return self
        pass
    def jugar(self):
        self.salud +=5
        self.energia -=10
        pass
    def sonido(self):
        print(self.sonido)
        pass