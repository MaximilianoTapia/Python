<<<<<<< HEAD

local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"



# en el mismo archivo, agrega lo siguiente debajo de la clase Usuario
print(square(5))
user = Usuario("Anna")
print(Anna.name)
print(usuario.di_hola())

=======
local_val = "unicornios mágicos"

def square(x):
    return x * x

class Usuario:
    def __init__(self, name):
        self.name = name
    
    def di_hola(self):
        return "hola"

print(square(5))
user = Usuario("Anna")
print(user.name)
print(user.di_hola())

if __name__ == "__main__":
    print("El archivo se está ejecutando directamente")
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)


>>>>>>> 4df5c425a2022e3c17fc5709bce2736c4a3ed089
