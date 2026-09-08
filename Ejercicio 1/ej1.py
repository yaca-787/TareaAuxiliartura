class Vehiculo:
    def __init__(self, marca, modelo, anio, kilometraje, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = color

    def mostrarKilometraje(self):
        kilometros = self.kilometraje // 1000
        metros = self.kilometraje % 1000
        print("Kilometraje:", kilometros, "km y", metros, "m")

    def cambiarColor(self, color):
        self.color = color

    def mostrarDatos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.anio)
        print("Color:", self.color)
        self.mostrarKilometraje()


auto1 = Vehiculo("Toyota", "Corolla", 2020, 12500, "Rojo")
auto2 = Vehiculo("Ford", "Mustang", 2022, 8700, "Azul")

auto1.cambiarColor("Negro")
auto2.cambiarColor("Blanco")

auto1.mostrarDatos()
print()
auto2.mostrarDatos()
