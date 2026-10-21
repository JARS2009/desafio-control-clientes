import datos
from clientes import buscar_indice_cliente
from utilidades import (titulo, linea, pausar, leer_texto, leer_decimal,
                        leer_entero, recortar, confirmar)


def nombre_cliente(ruc):
    indice = buscar_indice_cliente(ruc)
    if indice == -1:
        return "(no registrado)"
    return datos.clientes[indice][1]


def mostrar_tabla_servicios(indices):
    linea("-")
    print(f"{'N°':<4} {'RUC':<12} {'CLIENTE':<18} {'SERVICIO':<22} "
          f"{'COSTO':>10} {'ESTADO':<10} {'PAGO':<10}")
    linea("-")

    total = 0
    total_pagado = 0
    total_pendiente = 0

    if len(indices) == 0:
        print("No se encontraron servicios.")

    for i in indices:
        servicio = datos.servicios[i]
        print(f"{i + 1:<4} {servicio[0]:<12} {recortar(nombre_cliente(servicio[0]), 18):<18} "
              f"{recortar(servicio[1], 22):<22} {servicio[2]:>10.2f} "
              f"{servicio[3]:<10} {servicio[4]:<10}")
        total = total + servicio[2]
        if servicio[4] == datos.PAGADO:
            total_pagado = total_pagado + servicio[2]
        else:
            total_pendiente = total_pendiente + servicio[2]

    linea("-")
    print(f"Servicios: {len(indices)}   Total: S/ {total:.2f}   "
          f"Pagado: S/ {total_pagado:.2f}   Pendiente: S/ {total_pendiente:.2f}")


def todos_los_indices():
    indices = []
    for i in range(len(datos.servicios)):
        indices.append(i)
    return indices


def filtrar(posicion, valor):
    indices = []
    for i in range(len(datos.servicios)):
        if datos.servicios[i][posicion] == valor:
            indices.append(i)
    return indices


def buscar_por_texto(texto):
    texto = texto.lower()
    indices = []
    for i in range(len(datos.servicios)):
        servicio = datos.servicios[i]
        if texto in servicio[1].lower() or texto in nombre_cliente(servicio[0]).lower():
            indices.append(i)
    return indices


def ver_servicios():
    opcion = ""
    while opcion != "0":
        titulo("VER SERVICIOS")
        print("1. Todos los servicios")
        print("2. Pagos pendientes")
        print("3. Servicios pagados")
        print("4. Servicios concluidos")
        print("5. Servicios pendientes (por concluir)")
        print("6. Servicios de un cliente (por RUC)")
        print("7. Buscar servicio (descripción o cliente)")
        print("0. Volver")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            titulo("TODOS LOS SERVICIOS")
            mostrar_tabla_servicios(todos_los_indices())
        elif opcion == "2":
            titulo("SERVICIOS CON PAGO PENDIENTE")
            mostrar_tabla_servicios(filtrar(4, datos.PENDIENTE))
        elif opcion == "3":
            titulo("SERVICIOS PAGADOS")
            mostrar_tabla_servicios(filtrar(4, datos.PAGADO))
        elif opcion == "4":
            titulo("SERVICIOS CONCLUIDOS")
            mostrar_tabla_servicios(filtrar(3, datos.CONCLUIDO))
        elif opcion == "5":
            titulo("SERVICIOS POR CONCLUIR")
            mostrar_tabla_servicios(filtrar(3, datos.PENDIENTE))
        elif opcion == "6":
            ruc = leer_texto("RUC del cliente: ")
            titulo("SERVICIOS DE: " + nombre_cliente(ruc))
            mostrar_tabla_servicios(filtrar(0, ruc))
        elif opcion == "7":
            texto = leer_texto("Texto a buscar: ")
            titulo("RESULTADO DE LA BÚSQUEDA: " + texto)
            mostrar_tabla_servicios(buscar_por_texto(texto))
        elif opcion != "0":
            print("Opción inválida.")

        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            pausar()


def nuevo_servicio():
    titulo("NUEVO SERVICIO")

    ruc = leer_texto("RUC del cliente : ")
    while buscar_indice_cliente(ruc) == -1:
        print("  No existe un cliente con ese RUC. Regístrelo primero en Clientes.")
        if not confirmar("¿Intentar con otro RUC?"):
            return
        ruc = leer_texto("RUC del cliente : ")

    print("Cliente         :", nombre_cliente(ruc))
    descripcion = leer_texto("Servicio        : ")
    costo = leer_decimal("Costo (S/)      : ")

    datos.servicios.append([ruc, descripcion, costo, datos.PENDIENTE, datos.PENDIENTE])
    print("\nServicio registrado correctamente.")
    pausar()


def elegir_servicio(mensaje):
    if len(datos.servicios) == 0:
        print("No hay servicios registrados.")
        pausar()
        return -1
    mostrar_tabla_servicios(todos_los_indices())
    numero = leer_entero(mensaje + " (0 para cancelar): ", 0, len(datos.servicios))
    return numero - 1


def cambiar_estado_servicio():
    titulo("CAMBIAR ESTADO DEL SERVICIO")
    indice = elegir_servicio("N° de servicio")
    if indice == -1:
        return

    servicio = datos.servicios[indice]
    print("\nServicio:", servicio[1], "| Estado actual:", servicio[3])
    print("1.", datos.PENDIENTE)
    print("2.", datos.CONCLUIDO)
    estado = leer_entero("Nuevo estado: ", 1, 2)

    if estado == 1:
        servicio[3] = datos.PENDIENTE
    else:
        servicio[3] = datos.CONCLUIDO
    print("Estado actualizado a", servicio[3])
    pausar()


def registrar_pago():
    titulo("REGISTRAR PAGO")
    indice = elegir_servicio("N° de servicio a pagar")
    if indice == -1:
        return

    servicio = datos.servicios[indice]
    if servicio[4] == datos.PAGADO:
        print("\nEste servicio ya está pagado.")
    else:
        print(f"\nServicio: {servicio[1]} | Monto a pagar: S/ {servicio[2]:.2f}")
        print("(Solo se aceptan pagos completos)")
        if confirmar("¿Confirmar pago completo?"):
            servicio[4] = datos.PAGADO
            print("Pago registrado correctamente.")
        else:
            print("Pago cancelado.")
    pausar()


def menu_servicios():
    opcion = ""
    while opcion != "0":
        titulo("MENÚ SERVICIOS")
        print("1. Ver servicios (filtros y búsqueda)")
        print("2. Nuevo servicio")
        print("3. Cambiar estado del servicio")
        print("4. Registrar pago")
        print("0. Volver al menú principal")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            ver_servicios()
        elif opcion == "2":
            nuevo_servicio()
        elif opcion == "3":
            cambiar_estado_servicio()
        elif opcion == "4":
            registrar_pago()
        elif opcion != "0":
            print("Opción inválida.")
