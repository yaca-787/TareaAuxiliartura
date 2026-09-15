class SerVivo:
    def __init__(self, edad):
        self.edad = edad


class Animal(SerVivo):
    def __init__(self, edad, peso):
        super().__init__(edad)
        self.peso = peso


class Felino(Animal):
    def __init__(self, edad, peso, pelaje):
        super().__init__(edad, peso)
        self.pelaje = pelaje


class Gato(Felino):
    def __init__(self, edad, peso, pelaje, raza):
        super().__init__(edad, peso, pelaje)
        self.raza = raza

    def mostrar(self):
        print("Gato")
        print("Edad:", self.edad)
        print("Peso:", self.peso)
        print("Pelaje:", self.pelaje)
        print("Raza:", self.raza)


class Leon(Felino):
    def __init__(self, edad, peso, pelaje, melena):
        super().__init__(edad, peso, pelaje)
        self.melena = melena


class Reptil(Animal):
    def __init__(self, edad, peso, escamas):
        super().__init__(edad, peso)
        self.escamas = escamas


class Vibora(Reptil):
    def __init__(self, edad, peso, escamas, venenosa):
        super().__init__(edad, peso, escamas)
        self.venenosa = venenosa


class Roedor(Animal):
    def __init__(self, edad, peso, dientes):
        super().__init__(edad, peso)
        self.dientes = dientes


class Raton(Roedor):
    def __init__(self, edad, peso, dientes, color):
        super().__init__(edad, peso, dientes)
        self.color = color


class Conejo(Roedor):
    def __init__(self, edad, peso, dientes, raza):
        super().__init__(edad, peso, dientes)
        self.raza = raza


class Rana(Animal):
    def __init__(self, edad, peso, habitat):
        super().__init__(edad, peso)
        self.habitat = habitat


class Planta(SerVivo):
    def __init__(self, edad, altura):
        super().__init__(edad)
        self.altura = altura


class Flor(Planta):
    def __init__(self, edad, altura, color):
        super().__init__(edad, altura)
        self.color = color


class Humano(SerVivo):
    def __init__(self, edad, nombre):
        super().__init__(edad)
        self.nombre = nombre


class Nino(Humano):
    pass


class Adulto(Humano):
    pass


class Anciano(Humano):
    pass

gato = Gato(3, 5, "Corto", "Persa")
gato.mostrar()