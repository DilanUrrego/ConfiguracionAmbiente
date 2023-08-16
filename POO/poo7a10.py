class CuentaBancaria:
    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self, deposito):
        self.balance += deposito
        print("Se han depositado:", deposito, "el balance actual es:", self.balance)
    
    def retirar(self, retiro):
        self.balance -= retiro
        print("Se han retirado:", retiro, "el balance actual es:", self.balance)
    
    def mostrar_detalles(self):
        print(self.numero_cuenta, self.propietario, self.balance)

cuenta = CuentaBancaria("2425121418", "Dilan Urrego", 200000)
cuenta.depositar(50000)
cuenta.retirar(15000)
cuenta.mostrar_detalles()