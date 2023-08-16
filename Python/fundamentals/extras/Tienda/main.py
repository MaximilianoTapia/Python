from Tienda import tienda
from Producto import producto


def mostrar_menu():

    tienda1 = tienda("Tienda CR7")

    while True:
        print("*-------------- Tienda ---------------*")
        print("|| OPCIÓN 1: agregar producto        ||")
        print("|| OPCIÓN 2: vender producto         ||")
        print("|| OPCIÓN 3: listar productos        ||")
        print("|| OPCIÓN 0: Salir                   ||")
        print("*-------------------------------------*")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
                
            a = input("ingresa el nombre de producto: ")
            b = input("ingresa el precio de producto: ")
            c = input("Ingrese la categoria del producto: ")
            nuevo_producto = producto(a,b,c)
            print(f"los valores ingresados son {a}  {b}  {c} ")
            tienda1.agregar_producto(nuevo_producto)
            
        elif opcion == "2":
                
            a = input("")
            b = input("")
            c = input("")
            vender_producto = producto(a,b,c)
            print(f"los valores quitados son {a} {b} {c}")


        elif opcion == "3":
            tienda1.listar_producto()

        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ =="__main__":
    mostrar_menu()