
class producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else :
            self.precio -= self.precio * cambio_porcentaje / 100

    def imprimir(self):
        print(F"el nombre del producto es {self.nombre} el nombre de la categoria {self.categoria} el precio es {self.precio}")
