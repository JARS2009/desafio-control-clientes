import datos
from utilidades import titulo, linea, pausar, leer_texto, recortar


def buscar_indice_cliente(ruc):
    for i in range(len(datos.clientes)):
        if datos.clientes[i][0] == ruc:
            return i
    return -1


def calcular_totales(ruc):
    total_pagado = 0
    total_pendiente = 0
    for servicio in datos.servicios:
        if servicio[0] == ruc:
            if servicio[4] == datos.PAGADO:
                total_pagado = total_pagado + servicio[2]
            else:
                total_pendiente = total_pendiente + servicio[2]
    return total_pagado, total_pendiente


def mostrar_tabla_clientes(lista):
    linea("-")
    print(f"{'RUC':<12} {'RAZÓN SOCIAL':<24} {'DIRECCIÓN':<20} {'TELÉFONO':<10} "
          f"{'PAGADO':>10} {'PENDIENTE':>10}")
    linea("-")

    if len(lista) == 0:
        print("No se encontraron clientes.")

    for cliente in lista:
        pagado, pendiente = calcular_totales(cliente[0])
        print(f"{cliente[0]:<12} {recortar(cliente[1], 24):<24} "
              f"{recortar(cliente[2], 20):<20} {recortar(cliente[3], 10):<10} "
              f"{pagado:>10.2f} {pendiente:>10.2f}")
    linea("-")
    print("Total de clientes:", len(lista))


def buscar_cliente():
    texto = leer_texto("Ingrese RUC o razón social a buscar: ").lower()

    encontrados = []
    for cliente in datos.clientes:
        if texto in cliente[0] or texto in cliente[1].lower():
            encontrados.append(cliente)

    titulo("RESULTADO DE LA BÚSQUEDA: " + texto)
    mostrar_tabla_clientes(encontrados)
    pausar()


def ver_clientes():
    opcion = ""
    while opcion != "0":
        titulo("LISTA DE CLIENTES")
        mostrar_tabla_clientes(datos.clientes)
        print("\n1. Buscar cliente")
        print("0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            buscar_cliente()
        elif opcion != "0":
            print("Opción inválida.")


def ruc_valido(ruc):
    if len(ruc) != 11 or not ruc.isdigit():
        print("  El RUC debe tener 11 dígitos numéricos.")
        return False
    if buscar_indice_cliente(ruc) != -1:
        print("  Ya existe un cliente con ese RUC.")
        return False
    return True


def nuevo_cliente():
    titulo("NUEVO CLIENTE")

    ruc = input("RUC (11 dígitos) : ").strip()
    while not ruc_valido(ruc):
        ruc = input("RUC (11 dígitos) : ").strip()

    razon_social = leer_texto("Razón social     : ")
    direccion = leer_texto("Dirección        : ")
    telefono = leer_texto("Teléfono         : ")

    datos.clientes.append([ruc, razon_social, direccion, telefono])
    print("\nCliente registrado correctamente.")
    pausar()


def menu_clientes():
    opcion = ""
    while opcion != "0":
        titulo("MENÚ CLIENTES")
        print("1. Ver clientes")
        print("2. Nuevo cliente")
        print("0. Volver al menú principal")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            nuevo_cliente()
        elif opcion != "0":
            print("Opción inválida.")
