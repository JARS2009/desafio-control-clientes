ANCHO = 92


def linea(caracter="="):
    print(caracter * ANCHO)


def titulo(texto):
    print()
    linea()
    print(texto.center(ANCHO))
    linea()


def pausar():
    input("\nPresione ENTER para continuar...")


def recortar(texto, largo):
    if len(texto) <= largo:
        return texto
    return texto[:largo - 3] + "..."


def leer_texto(mensaje):
    texto = input(mensaje).strip()
    while texto == "":
        print("  El dato no puede estar vacío.")
        texto = input(mensaje).strip()
    return texto


def leer_decimal(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            print("  El monto debe ser mayor a 0.")
        except ValueError:
            print("  Ingrese un número válido.")


def leer_entero(mensaje, minimo, maximo):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            numero = int(valor)
            if numero >= minimo and numero <= maximo:
                return numero
        print("  Ingrese un número entre", minimo, "y", maximo)


def confirmar(mensaje):
    respuesta = input(mensaje + " (S/N): ").strip().upper()
    return respuesta == "S"
