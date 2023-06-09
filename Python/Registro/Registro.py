class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Registro:
    def __init__(self, usuario, tiempo, tipo):
        self.usuario = usuario
        self.tiempo = tiempo
        self.tipo = tipo


class SistemaAsistencia:
    def __init__(self):
        self.usuarios = []
        self.registros = []

    def agregar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print(f"Usuario {nombre} agregado.")

    def registrar_entrada(self, nombre):
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            registro = Registro(usuario, "now", "entrada")
            self.registros.append(registro)
            print(f"Registro de entrada para {nombre} creado.")
        else:
            print(f"No se encontró el usuario {nombre}.")

    def registrar_salida(self, nombre):
        usuario = self.encontrar_usuario(nombre)
        if usuario:
            registro = Registro(usuario, "now", "salida")
            self.registros.append(registro)
            print(f"Registro de salida para {nombre} creado.")
        else:
            print(f"No se encontró el usuario {nombre}.")

    def listar_registros(self):
        print("Registros de asistencia:")
        for registro in self.registros:
            print(f"{registro.usuario.nombre} - {registro.tiempo} - {registro.tipo}")

    def encontrar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None


def main():
    sistema_asistencia = SistemaAsistencia()

    while True:
        print("=== Sistema de Asistencia ===")
        print("1. =====Agregar Usuario======")
        print("2. =====Registrar Entrada====")
        print("3. =====Registrar Salida=====")
        print("4. =====Listar Registros=====")
        print("5. ==========Salir===========")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.agregar_usuario(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_entrada(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema_asistencia.registrar_salida(nombre)
        elif opcion == "4":
            sistema_asistencia.listar_registros()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()

