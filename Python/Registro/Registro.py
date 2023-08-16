class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    

class Registro:
    def __init__(self, persona, tiempo,tipo):
        self.persona = persona
        self.tiempo = tiempo
        self.tipo = tipo

class Sistemasitencia:
    def __init__(self):
        self.Persona = []
        self.Registro = []
    
    def agregar_personas(self, nombre):
        persona = Persona(nombre)
        self.Persona.append(persona)
        print(f"persona {nombre} agregado.")
    
    def registrar_entrada(self, nombre):
        persona = self.encontrar_Persona(nombre)
        if persona:
            Registro = Registro(persona,"now", "entrada")
            self.Registro.append(Registro)
            print(f"Registro de salida para {nombre} creado.")
        else:
            print(f"No se encontró la persona {nombre}.")

    def registrar_salida(self, nombre)