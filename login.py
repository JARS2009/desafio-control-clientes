import datos
from utilidades import titulo

MAX_INTENTOS = 3


def iniciar_sesion():
    intentos = 0
    while intentos < MAX_INTENTOS:
        titulo("INICIO DE SESIÓN")
        nombre = input("Usuario    : ").strip()
        clave = input("Contraseña : ").strip()

        if nombre == datos.usuario[0] and clave == datos.usuario[1]:
            print("\n¡Bienvenido,", nombre + "!")
            return True

        intentos = intentos + 1
        print("\nUsuario o contraseña incorrectos.")
        print("Intentos restantes:", MAX_INTENTOS - intentos)

    return False
