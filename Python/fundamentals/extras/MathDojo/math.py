class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.num = num
        self.num5 = nums
    def subtract(self, num, *nums):
        self.num = num
        self.num5 = nums
        # tu código aquí
# crear una instancia:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debería imprimir 5
# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado

