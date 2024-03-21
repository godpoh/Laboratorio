print("1. Visualizar estadio y precios de los asientos.")
print("2. Registro de espectadores.")
print("3. Compra de entradas.")
print("4. Reporte de Ventas")
print("5. Salir.")

while True:
    options = input("Escribe una de las opciones: ")

    if options == "1":
        print("Ha ingresado la opcion 1. ")

    elif options == "2":
        print("Ha ingresado la opcion 2. ")

    elif options == "3":
        print("Ha ingresado la opcion 3.")
        log_in = input("Ingrese su cedula para registrarse: ")
        while True:
            confirm = input(f"Su cedula es {log_in}? (S/N): ")
            if confirm.lower() == "s":
                print("prueba")
                while True:
                    buy_ticket_amount = input("Ingrese la cantidad de tickets que desea comprar: ")
                    if buy_ticket_amount <= 3:
                        pass
                    else:
                        pass
            elif confirm.lower() == "n":
                log_in = input("Digite correctamente su cedula: ")
            else:
                print("Opcion invalida")

    elif options == "4":
        print("Ha ingresado la opcion 4. ")

    elif options == "5":
        print("Ha ingresado la opcion 5. ")
        break
    else:
        print("Opcion invalida")


