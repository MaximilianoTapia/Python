<<<<<<< HEAD
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
        print("1. Agregar Usuario")
        print("2. Registrar Entrada")
        print("3. Registrar Salida")
        print("4. Listar Registros")
        print("5. Salir")

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
=======
class UsuarioExiste(Exception):
    pass

class UsuarioNoExiste(Exception):
    pass

class Usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def cambiar_password(self, nuevo_password):
        self.password = nuevo_password
        print("Contraseña cambiada exitosamente.")

class Invitado(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo, "invitado")

class Administrador(Usuario):
    def __init__(self, nombre, correo, password):
        super().__init__(nombre, correo, password)

    def eliminar_usuario(self, usuario, sistema):
        sistema.eliminar_usuario(usuario)

    def modificar_usuario(self, usuario, nuevo_nombre, nuevo_correo, sistema):
        if usuario not in sistema.usuarios:
            raise UsuarioNoExiste("El usuario no existe en el sistema.")
        usuario.nombre = nuevo_nombre
        usuario.correo = nuevo_correo
        print("Usuario modificado exitosamente.")

    def listar_usuarios(self, sistema):
        print("Lista de usuarios:")
        for usuario in sistema.usuarios:
            print(f"Nombre: {usuario.nombre} - Correo: {usuario.correo}")

class Sistema:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        for u in self.usuarios:
            if u.nombre == usuario.nombre:
                raise UsuarioExiste("El usuario ya existe en el sistema.")
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        if usuario not in self.usuarios:
            raise UsuarioNoExiste("El usuario no existe en el sistema.")
        self.usuarios.remove(usuario)


def main():
    # Interfaz de la consola
    sistema = Sistema()

    while True:

        print("********************************s****** ")
        print("******Sistema Gestión de Usuarios****** ")
        print("********************************s****** ")
        print("1. Crear un usuario")
        print("2. Cambiar contraseña")
        print("3. Modificar usuario")
        print("4. Listar usuarios")
        print("5. Salir")
        option = input("Elige una opción: ")

        try:
            if option == "1":
                nombre = input("Ingresa el nombre: ")
                correo = input("Ingresa el correo: ")
                password = input("Ingresa la contraseña: ")
                nuevo_usuario = Usuario(nombre, correo, password)
                sistema.agregar_usuario(nuevo_usuario)

            elif option == "2":
                nombre = input("Ingresa tu nombre: ")
                for usuario in sistema.usuarios:
                    if usuario.nombre == nombre:
                        nuevo_password = input("Ingresa tu nueva contraseña: ")
                        usuario.cambiar_password(nuevo_password)
                        break
                else:
                    raise UsuarioNoExiste(
                        "El usuario no existe en el sistema.")

            elif option == "3":
                nombre = input("Ingresa el nombre del usuario a modificar: ")
                for usuario in sistema.usuarios:
                    if usuario.nombre == nombre:
                        nuevo_nombre = input("Ingresa el nuevo nombre: ")
                        nuevo_correo = input("Ingresa el nuevo correo: ")
                        administrador = Administrador("", "", "")
                        administrador.modificar_usuario(
                            usuario, nuevo_nombre, nuevo_correo, sistema)
                        break
                else:
                    raise UsuarioNoExiste(
                        "El usuario no existe en el sistema.")

            elif option == "4":
                administrador = Administrador("", "", "")
                administrador.listar_usuarios(sistema)

            elif option == "5":
                break
        except UsuarioExiste as ue:
            print(ue)
        except UsuarioNoExiste as une:
            print(une)


if __name__ == "__main__":
    main()
>>>>>>> 4df5c425a2022e3c17fc5709bce2736c4a3ed089
