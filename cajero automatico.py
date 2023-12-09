class CajeroAutomatico:
    def __init__(self, numero_tarjeta, contrasena, saldo_inicial=5000):
        self.numero_tarjeta = numero_tarjeta
        self.contrasena = contrasena
        self.saldo = saldo_inicial

    def verificar_tarjeta(self, numero_tarjeta, contrasena):
        return self.numero_tarjeta == numero_tarjeta and self.contrasena == contrasena

    def consultar_saldo(self):
        return f"Tu saldo actual es: ${self.saldo}"

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo}"
        else:
            return "Error: El monto debe ser mayor que cero."

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro exitoso. Nuevo saldo: ${self.saldo}"
        elif monto <= 0:
            return "Error: El monto debe ser mayor que cero."
        else:
            return "Error: Fondos insuficientes."

def main():
    numero_tarjeta = "8093592369"
    contrasena = "1234"

    cajero = CajeroAutomatico(numero_tarjeta, contrasena)

    input_tarjeta = input("Ingrese el número de tarjeta: ")
    input_contrasena = input("Ingrese la contraseña: ")

    if cajero.verificar_tarjeta(input_tarjeta, input_contrasena):
        print("Validación exitosa. ¡Bienvenido Jhoan Bonilla !\n")
    else:
        print("validación fallida. Saliendo del sistema.")
        return

    while True:
        print("\n1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(cajero.consultar_saldo())
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            print(cajero.depositar(monto))
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            print(cajero.retirar(monto))
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
