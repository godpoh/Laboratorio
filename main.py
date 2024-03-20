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
        soccer_field = [
            "10A", "10B", "10C","10D", "10E", "10F", "10G", "10H", "10I", "10J",
            "9A ", "9B ", "9C ","9D ", "9E ", "9F ", "9G ", "9H ", "9I ", "9J",
            "8A ", "8B ", "8C ","8D ", "8E ", "8F ", "8G ", "8H ", "8I ", "8J",
            "7A ", "7B ", "7C ","7D ", "7E ", "7F ", "7G ", "7H ", "7I ", "7J",
            "6A ", "6B ", "6C ","6D ", "6E ", "6F ", "6G ", "6H ", "6I ", "6J",
            "5A ", "5B ", "5C ","5D ", "5E ", "5F ", "5G ", "5H ", "5I ", "5J",
            "4A ", "4B ", "4C ","4D ", "4E ", "4F ", "4G ", "4H ", "4I ", "4J",
            "3A ", "3B ", "3C ","3D ", "3E ", "3F ", "3G ", "3H ", "3I ", "3J",
            "2A ", "2B ", "2C ","2D ", "2E ", "2F ", "2G ", "2H ", "2I ", "2J",
            "1A ", "1B ", "1C ","1D ", "1E ", "1F ", "1G ", "1H ", "1I ", "1J"
        ]

    elif options == "3":
        print("Ha ingresado la opcion 3.")
        log_in = input("Ingrese su cedula para registrarse: ")
        while True:
            confirm = input(f"Su cedula es {log_in}? (S/N): ")
            if confirm.lower() == "s":
                print("prueba")
                break
            elif confirm.lower() == "n":
                log_in = input("Digite correctamente su cedula: ")
            else:
                print("Opcion invalida")

        buy_ticket_amount = input("Ingrese la cantidad de tickets que desea comprar: ")

    elif options == "4":
        print("Ha ingresado la opcion 4. ")

    elif options == "5":
        print("Ha ingresado la opcion 5. ")
        break
    else:
        print("Opcion invalida")





