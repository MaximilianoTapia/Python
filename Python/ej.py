class Calculadora:
    def __init__(self):
        self.operacion = ""

    def sumar(self, a, b):
        self.operacion = f"{a} + {b}"
        return a + b

    def restar(self, a, b):
        self.operacion = f"{a} - {b}"
        return a - b

    def multiplicar(self, a, b):
        self.operacion = f"{a} * {b}"
        return a * b

    def dividir(self, a, b):
        if b != 0:
            self.operacion = f"{a} / {b}"
            return a / b
        else:
            return "Error: No se puede dividir entre cero."


def mostrar_menu():
    print("*------ Calculadora -------*")
    print("|| OPCIÓN 1: Sumar        ||")
    print("|| OPCIÓN 2: Restar       ||")
    print("|| OPCIÓN 3: Multiplicar  ||")
    print("|| OPCIÓN 4: Dividir      ||")
    print("|| OPCIÓN 0: Salir        ||")
    print("*--------------------------*")


# Ejemplo de uso:
calculadora = Calculadora()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = calculadora.sumar(a, b)
        print(f"Resultado de la suma {a} + {b} es: {resultado}\n")

    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = calculadora.restar(a, b)
        print(f"Resultado: {resultado}\n")

    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = calculadora.multiplicar(a, b)
        print(f"Resultado: {resultado}\n")

    elif opcion == "4":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = calculadora.dividir(a, b)
        print(f"Resultado: {resultado}\n")

    elif opcion == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.\n")