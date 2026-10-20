import datos
from utilidades import linea, ANCHO
from login import iniciar_sesion
from clientes import menu_clientes
from servicios import menu_servicios
from configuracion import menu_configuracion


def mostrar_cabecera():
    print()
    linea()
    print(datos.empresa[0].upper().center(ANCHO))
    print(("Dirección: " + datos.empresa[1]).center(ANCHO))
    print(("Teléfono: " + datos.empresa[2]).center(ANCHO))
    linea()


def menu_principal():
    opcion = ""
    while opcion != "0":
        mostrar_cabecera()
        print("MENÚ PRINCIPAL")
        print("1. Clientes")
        print("2. Servicios")
        print("3. Configuración")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_servicios()
        elif opcion == "3":
            menu_configuracion()
        elif opcion == "0":
            print("\n¡Hasta pronto!")
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    if iniciar_sesion():
        menu_principal()
    else:
        print("\nDemasiados intentos fallidos. El programa se cerrará.")
