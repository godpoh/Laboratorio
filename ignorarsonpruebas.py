import random
import time
import json
from datetime import datetime

class Estadio:
    def __init__(self):
        self.filename = 'manager.json'
        with open(self.filename, 'r') as file:
            self.data = json.load(file)
        self.ocupados = {(asiento['fila'], asiento['columna']) for asiento in self.data['ocupados']}

    def visualizar_estadio_precios(self):
        rows = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
        columns = ['A', 'B', 'C', 'D', 'E', 'F', "G", 'H', 'I', 'J']
        prices = {8: 15000, 7: 15000, 6: 15000, 5: 10000, 4: 5000, 3: 5000, 2: 5000, 1: 5000}

        for row in rows:
            for column in columns:
                if (row, column) in self.ocupados:
                    print("\033[91m" + row + column, end=' ')
                else:
                    print("\033[92m" + row + column, end=' ')
            print()

        print("Precios de los asientos:")
        for fila, precio in prices.items():
            print(f"Fila {fila}: {precio} colones")

    def registro_espectadores(self):
        espectadores = []
        while True:
            cedula = input("Introduzca su cedula (o 'q' para salir): ")
            if cedula.lower() == 'q':
                break
            nombre = input("Introduzca su nombre: ")
            genero = input("Introduzca su género: ")
            espectadores.append({'cedula': cedula, 'nombre': nombre, 'genero': genero})
        return espectadores

    def compra_entradas(self, espectadores):
        total = 0
        for espectador in espectadores:
            print(f"\nCompra de entradas para {espectador['nombre']}:")
            for _ in range(3):  # Límite de 3 boletos por persona
                fila = input("Introduzca la fila del asiento (1-10): ")
                columna = input("Introduzca la columna del asiento (A-J): ")
                if (fila, columna) in self.ocupados:
                    print("Lo siento, ese asiento ya está ocupado.")
                else:
                    self.ocupados.add((fila, columna))
                    total += self.calcular_precio(int(fila))
                    print(f"Asiento {fila}{columna} comprado con éxito.")
        return total

    def calcular_precio(self, fila):
        if fila >= 8:
            return 15000
        elif fila >= 5:
            return 10000
        else:
            return 5000

    def reporte_ventas(self, espectadores, total):
        print("\nReporte de Ventas:")
        print("Cantidad de boletos comprados por género:")
        generos = {'Masculino': 0, 'Femenino': 0, 'Otro': 0}
        for espectador in espectadores:
            generos[espectador['genero']] += 3  # Se asume que cada persona compra 3 boletos
        for genero, cantidad in generos.items():
            print(f"{genero}: {cantidad}")
        print(f"Monto total de ventas: {total} colones")
        print(f"Fecha y hora de la compra: {datetime.now()}")

    def guardar_estado(self):
        with open(self.filename, 'w') as file:
            json.dump({'ocupados': [{'fila': fila, 'columna': columna} for fila, columna in self.ocupados]}, file)

    def ejecutar(self):
        while True:
            print("\nMenú del Sistema:")
            print("1. Visualizar estadio y precios de los asientos.")
            print("2. Registro de espectadores.")
            print("3. Compra de entradas.")
            print("4. Reporte de Ventas")
            print("5. Salir.")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.visualizar_estadio_precios()
            elif opcion == "2":
                espectadores = self.registro_espectadores()
            elif opcion == "3":
                if not espectadores:
                    print("Primero debe registrar espectadores.")
                else:
                    total_venta = self.compra_entradas(espectadores)
                    self.guardar_estado()
                    self.reporte_ventas(espectadores, total_venta)
            elif opcion == "4":
                if not espectadores:
                    print("Primero debe registrar espectadores y realizar compras.")
                else:
                    self.reporte_ventas(espectadores, 0)
            elif opcion == "5":
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")

estadio = Estadio()
estadio.ejecutar()
