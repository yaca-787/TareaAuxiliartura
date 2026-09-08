class CuentaBancaria:
    def __init__(self, titular, nroCuenta, saldo):
        self.titular = titular
        self.nroCuenta = nroCuenta
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            print("ERROR: El monto debe ser mayor que 0.")
        else:
            self.saldo = self.saldo + monto
            print("Se depositó:", monto, "Bs.")
            print("Saldo actual:", self.saldo, "Bs.")

    def retirar(self, monto):
        if monto <= 0:
            print("ERROR: El monto debe ser mayor que 0.")
        elif monto > self.saldo:
            print("ERROR: No puedes retirar más dinero del disponible.")
            print("Saldo disponible:", self.saldo, "Bs.")
        else:
            self.saldo = self.saldo - monto
            print("Se retiró:", monto, "Bs.")
            print("Saldo restante:", self.saldo, "Bs.")

    def mostrarDatos(self):
        print("\n--- DATOS DE LA CUENTA ---")
        print("Titular:", self.titular)
        print("Nro. de cuenta:", self.nroCuenta)
        print("Saldo:", self.saldo, "Bs.")


# Datos de la cuenta
cuenta = CuentaBancaria("Juan", "123456", 1000)

opcion = 0

while opcion != 4:

    print("\n--- CUENTA BANCARIA ---")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar datos")
    print("4. Salir")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        monto = float(input("Ingrese el monto a depositar: "))
        cuenta.depositar(monto)

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta.retirar(monto)

    elif opcion == 3:
        cuenta.mostrarDatos()

    elif opcion == 4:
        print("Programa finalizado.")

    else:
        print("ERROR: Opción no válida.")
