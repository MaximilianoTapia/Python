""""agregar_producto(self, nuevo_producto): toma un producto y lo agrega a la tienda
vender_producto(self, id): elimina el producto de la lista de productos de la tienda mediante el id (supón que el id es el índice del producto en la lista) e imprime su información.
inflación(self, porcentaje_aumento): aumenta el precio de cada producto por el porcentaje_aumento dado (¡usa el método que escribiste en la clase Producto!)
hacer_liquidación(self, category, porcentaje_descuento): actualiza todos los productos que coinciden con la categoría dada al reducir el precio por el porcentaje_descuento dado (¡usa el método que escribiste en la clase Producto!) 
"""
class tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.list = []

    def agregar_producto(self, nuevo_producto):
        self.list.append(nuevo_producto)
        return self
    
    def vender_producto(self, id):
        for x in self.list:
            if x.nombre == id:
                x.remove
            else:
                print("producto no existe")
        return self
    def listar_producto(self):
        for x in self.list:
            x.imprimir()
        return self