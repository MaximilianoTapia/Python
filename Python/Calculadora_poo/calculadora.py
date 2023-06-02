class Calculadora:
    def __init__(self):
        self.ultimo_resultado = None

    def sumar(self, num1, num2):
        resultado = num1 + num2
        self.ultimo_resultado = resultado
        return resultado

    def restar(self, num1, num2):
        resultado = num1 - num2
        self.ultimo_resultado = resultado
        return resultado

    def multliplicar(self, num1, num2):
        resultado = num1 * num2
        self.ultimo_resultado = resultado
        return resultado

    def dividir(self, num1, num2):
        if num2 == 0:
            print("error")
            return None
        resultado = num1 / num2
        self.ultimo_resultado = resultado
        return resultado

"""calculadora = Calculadora()
print(calculadora.sumar(10, 7))
print(calculadora.ultimo_resultado)

print(calculadora.restar(26, 3))
print(calculadora.ultimo_resultado)

print(calculadora.multliplicar(7, 4))
print(calculadora.ultimo_resultado)

print(calculadora.dividir(24, 12))
print(calculadora.ultimo_resultado)

print(calculadora.dividir(10, 0))
print( calculadora.ultimo_resultado)
"""

def mostrar_menu():

    calculadora = Calculadora()

    while True:
        print("*------ Calculadora -------*")
        print("|| OPCIÓN 1: Sumar        ||")
        print("|| OPCIÓN 2: Restar       ||")
        print("|| OPCIÓN 3: Multiplicar  ||")
        print("|| OPCIÓN 4: Dividir      ||")
        print("|| OPCIÓN 0: Salir        ||")
        print("*--------------------------*")

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

if __name__ =="__main__":
    mostrar_menu()