class MathDojo:
    def __init__(self):
        self.result = 0
    
    def sumar(self, *args):
        for num in args:
            self.result += num
        return self
    
    def restar(self, *args):
        for num in args:
            self.result -= num
        return self

# Pruebas
md = MathDojo()

# Sumar
resultado_suma1 = md.sumar(5, 10).sumar(20).sumar(30, 15).result
print("Resultado de la suma 1:", resultado_suma1)  # Debería ser 80

resultado_suma2 = md.sumar(8, 12, 6).sumar(10).result
print("Resultado de la suma 2:", resultado_suma2)  # Debería ser 116

# Restar
resultado_resta1 = md.restar(10, 5).restar(8).restar(15, 7).result
print("Resultado de la resta 1:", resultado_resta1)  # Debería ser 71

resultado_resta2 = md.restar(20, 15, 3).restar(10).result
print("Resultado de la resta 2:", resultado_resta2)  # Debería ser 43
