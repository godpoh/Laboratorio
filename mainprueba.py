import random
import time
from colorama import Fore, init
import random as rd
init(autoreset=True)

class main:
    def __init__(self):
        self.main = []
        self.matriz = None

    def principal_menu(self):
        while True:
            print("\n")
            print("----------------------------------------------------")
            print("1. Visualizar estadio y precios de los asientos.")
            print("2. Registro de espectadores.")
            print("3. Compra de entradas.")
            print("4. Reporte de Ventas")
            print("5. Salir.")
            print("----------------------------------------------------")
            options = input("Selecciona una opcion: ")

            if options == "1":
                self.startstadium_price_seats()
            if options == "2":
                self.viewers_count()
            if options == "3":
                self.buy_tickets()
            if options == "4":
                self.ticket_sale()
            if options == "5":
                break

    def startstadium_price_seats(self):
        matriz = []
        rows = "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"
        columns = 'A', 'B', 'C', 'D', 'E', 'F', "G", 'H', 'I', 'J'

        red_seats = set()
        while len(red_seats) < 15:
            red_seats.add((random.choice(rows), random.choice(columns)))

        for row in rows:
            for column in columns:
                if (row, column) in red_seats:
                    print(Fore.RED + row + column, end=' ')
                else:
                    print(Fore.GREEN + row + column, end=' ')
            print()
        optional = input("Desea ver los precios de los asientos?(SI/NO,VOLVERA AL MENU PRINCIPAL): ")

        while True:
            if optional.lower() == 'si':
                print("\n")
                print("----------------------------------------------------")
                print("De la fila 10 a 8 el precio es de 15000 Colones")
                print("De la fila 5 a 7 el precio es de 10000 Colones")
                print("De la fila 1 a 4 el precio es de 5000 Colones")
                print("----------------------------------------------------")
                print("Volviendo al menu principal")
                time.sleep(12)
                return
            elif optional.lower() == 'no':
                print("Volviendo al menu principal...")
                time.sleep(5)
                return
            else:
                optional = input("Introduzca SI ó NO: ")

    def viewers_count(self):
        pass
    def buy_tickets(self):
        pass

    def ticket_sale(self):
        pass

test = main()
test.principal_menu()

