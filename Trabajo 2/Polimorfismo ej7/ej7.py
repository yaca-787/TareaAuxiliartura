class Auto:
    def __init__(self, marca="Toyota", color="Rojo", gasolina=0):
        self.marca = marca
        self.color = color
        self.gasolina = gasolina

    def __iadd__(self, litros):
        self.gasolina += litros
        return self

    def __add__(self, nuevo_color):
        self.color = nuevo_color
        return self

    def __sub__(self, otro):
        return self.gasolina + otro.gasolina

    def mostrar(self):
        print("Marca:", self.marca)
        print("Color:", self.color)
        print("Gasolina:", self.gasolina, "litros")
        print()

auto1 = Auto()
auto2 = Auto("Nissan", "Azul", 20)

print("AUTO 1")
auto1.mostrar()

print("AUTO 2")
auto2.mostrar()

auto1 += 5

print("AUTO 1 después de aumentar gasolina:")
auto1.mostrar()

auto1 + "Negro"

print("AUTO 1 después de cambiar el color:")
auto1.mostrar()

total = auto1 - auto2

print("Gasolina total de los 2 autos:", total, "litros")