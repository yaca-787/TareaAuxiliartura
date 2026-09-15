class Bus:
    def __init__(self, capacidad, pasajeros):
        self.capacidad = capacidad
        self.pasajeros = pasajeros
        self.dinero = 0
        self.costoPasaje = 1.50

    def subirPasajeros(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no válida.")
        elif self.pasajeros + cantidad > self.capacidad:
            print("No pueden subir todos los pasajeros.")
            print("Asientos disponibles:", self.capacidad - self.pasajeros)
        else:
            self.pasajeros = self.pasajeros + cantidad
            print("Subieron", cantidad, "pasajeros.")

    def cobrarPasaje(self):
        total = self.pasajeros * self.costoPasaje
        self.dinero = self.dinero + total
        print("Total recaudado:", total, "Bs.")

    def asientosDisponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos disponibles:", disponibles)


bus = Bus(40, 10)

print("Pasajeros iniciales:", bus.pasajeros)

x = int(input("Ingrese la cantidad de pasajeros que desean subir: "))

bus.subirPasajeros(x)

bus.asientosDisponibles()

bus.cobrarPasaje()

print("\nDatos finales del bus:")
print("Capacidad:", bus.capacidad)
print("Pasajeros:", bus.pasajeros)
print("Asientos disponibles:", bus.capacidad - bus.pasajeros)
print("Dinero recaudado:", bus.dinero, "Bs.")
