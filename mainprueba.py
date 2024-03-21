class node:
    def __init__(self):
        self.nodes = []

    def principal_menu(self):
        while True:
            print("1. Visualizar estadio y precios de los asientos.")
            print("2. Registro de espectadores.")
            print("3. Compra de entradas.")
            print("4. Reporte de Ventas")
            print("5. Salir.")

            options = input("Selecciona una opcion: ")

            if options == "1":
                self.startstadium()
            if options == "2":
                self.viewers_count()
            if options == "3":
                self.buy_tickets()
            if options == "4":
                self.ticket_sale()
            if options == "5":
                break

    def startstadium(self):
        matriz = []
        rows = "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"
        columns = 'A', 'B', 'C', 'D', 'E', 'F', "G", 'H', 'I', 'J'
        for row in rows:
            for colum in columns:
                print(row + colum, end=' ')
            print()

    def viewers_count(self):
        pass

    def buy_tickets(self):
        pass

    def ticket_sale(self):
        pass

test = node()
test.principal_menu()
test.startstadium()
