class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def mostrar_info(self):
        print(f"Nombre: {self.name}")
        print(f"Salud: {self.health}")
        print(f"Felicidad: {self.happiness}")

    def alimentar(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=80)
        self.roar_power = 8

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Poder de Rugido: {self.roar_power}")

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=95, happiness=75)
        self.stripe_count = 50

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Rayas: {self.stripe_count}")

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=85, happiness=90)
        self.hibernating = False

    def mostrar_info(self):
        super().mostrar_info()
        hibernating_status = "Sí" if self.hibernating else "No"
        print(f"¿Hibernando? {hibernating_status}")

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def agregar_león(self, name, age):
        self.animals.append(Lion(name, age))

    def agregar_tigre(self, name, age):
        self.animals.append(Tiger(name, age))

    def agregar_oso(self, name, age):
        self.animals.append(Bear(name, age))

    def imprimir_toda_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.mostrar_info()

zoo1 = Zoo("El zoo de John")
zoo1.agregar_león("Nala", 5)
zoo1.agregar_león("Simba", 6)
zoo1.agregar_tigre("Rajah", 4)
zoo1.agregar_tigre("Shere Khan", 7)
zoo1.agregar_oso("Baloo", 8)
zoo1.imprimir_toda_info()
