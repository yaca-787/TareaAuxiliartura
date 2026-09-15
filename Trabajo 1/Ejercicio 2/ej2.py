class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrarDatos(self):
        print("Marca:", self.marca)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram, "GB")
        print("Almacenamiento:", self.almacenamiento, "GB")

    def igualRAM(self, x):
        return self.ram == x


computadora1 = Computadora("HP", "Intel i5", 8, 512)
computadora2 = Computadora("Lenovo", "AMD Ryzen 5", 16, 1000)

computadora1.mostrarDatos()
print()
computadora2.mostrarDatos()

x = int(input("\nIngrese la cantidad de RAM X: "))

if computadora1.igualRAM(x):
    print("La computadora 1 tiene RAM igual a X.")

if computadora2.igualRAM(x):
    print("La computadora 2 tiene RAM igual a X.")

print("\nComputadora con mayor almacenamiento:")

if computadora1.almacenamiento > computadora2.almacenamiento:
    computadora1.mostrarDatos()
elif computadora2.almacenamiento > computadora1.almacenamiento:
    computadora2.mostrarDatos()
else:
    print("Las dos computadoras tienen el mismo almacenamiento.")
