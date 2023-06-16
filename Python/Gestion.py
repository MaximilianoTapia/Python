class Libro:
    def __init__(self, titulo, autor, isbn, año , estado):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.estado = estado

class Usuario:
    def __init__(self, usuario, id, lprestados):
        self.usuario = usuario
        self.id = id
        self.lprestados = lprestados

class Biblioteca:
    def __init__(self, libros, usuarios):
        self.libros = libros
        self.usuarios = usuarios


class Gestion:
    def __init__(self):
        self.usuarios = []
        self.libro = []
        self.biblioteca = []

    def agregar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} agregado.")

    def registrar_entrada(self, nombre):
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            usuario = Usuario(usuario, "now", "entrada")
            self.usuarios.append(usuario)
            print(f"Registro de entrada para {nombre} creado.")
        else:
            print(f"No se encontró el usuario {nombre}.")

    def registrar_salida(self, nombre):
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            usuario= Usuario(usuario, "now", "salida")
            self.usuarios.append(usuario)
            print(f"Registro de salida para {nombre} creado.")
        else:
            print(f"No se encontró el usuario {nombre}.")

    def listar_registros(self):
        print("Registros de asistencia:")
        for usuarios in self.usuarios:
            print(f"{usuarios.usuario.nombre} - {usuarios.tiempo} - {usuarios.tipo}")

    def encontrar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None


def main():
    gestion = Gestion()

    while True:
        print("====Sistema de Asistencia====")
        print("1. =====Agregar Libro========")
        print("2. =====Registrar Libro======")
        print("3. =====Registrar Libro======")
        print("4. =====Listar Libros========")
        print("5. ==========Salir===========")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del libro: ")
            gestion.agregar_usuario(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del libro: ")
            gestion.registrar_entrada(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del libro: ")
            gestion.registrar_salida(nombre)
        elif opcion == "4":
            gestion.listar_registros()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()