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



calculadora = Calculadora()
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

