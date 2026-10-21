import datos
from utilidades import titulo, pausar, leer_texto


def cambiar_accesos():
    titulo("CAMBIAR USUARIO Y CONTRASEÑA")

    actual = input("Contraseña actual: ").strip()
    if actual != datos.usuario[1]:
        print("La contraseña actual es incorrecta.")
        pausar()
        return

    nuevo_usuario = leer_texto("Nuevo usuario        : ")
    nueva_clave = leer_texto("Nueva contraseña     : ")
    repetir_clave = input("Repita la contraseña : ").strip()

    if nueva_clave != repetir_clave:
        print("Las contraseñas no coinciden. No se guardaron cambios.")
    else:
        datos.usuario[0] = nuevo_usuario
        datos.usuario[1] = nueva_clave
        print("Accesos actualizados correctamente.")
    pausar()


def cambiar_datos_empresa():
    titulo("CAMBIAR DATOS DE LA EMPRESA")
    print("Deje vacío y presione ENTER para mantener el dato actual.\n")

    campos = ["Nombre", "Dirección", "Teléfono"]
    for i in range(len(campos)):
        nuevo = input(f"{campos[i]} [{datos.empresa[i]}]: ").strip()
        if nuevo != "":
            datos.empresa[i] = nuevo

    print("\nDatos de la empresa actualizados.")
    pausar()


def menu_configuracion():
    opcion = ""
    while opcion != "0":
        titulo("CONFIGURACIÓN")
        print("1. Cambiar usuario y contraseña")
        print("2. Cambiar datos de la empresa")
        print("0. Volver al menú principal")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            cambiar_accesos()
        elif opcion == "2":
            cambiar_datos_empresa()
        elif opcion != "0":
            print("Opción inválida.")
