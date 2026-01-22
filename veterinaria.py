class CuentaBancaria:
    def __init__(self):
        # El balance siempre empieza en 0, no hace falta pedirlo al crear la cuenta
        self.balance = 0
        
    def depositar(self, cantidad):
        # Usamos += para sumar la cantidad al balance actual
        self.balance += cantidad
        print(f"Has depositado: {cantidad}")
    
    def ver_balance(self): 
        print(f"El valor que tienes en tu cuenta es: {self.balance}")
        
    def retirar(self,cantidad):
        if cantidad <= self.balance:
            self.balance -=cantidad
            print(f"Retiro Exitoso: {cantidad}")
        else:
            print("No es posible retirar este monto")
        
        
        
# --- CÓMO USAR LA CLASE ---
mi_cuenta = CuentaBancaria()

try:
    monto = int(input("Porfavor ingreas el valor a depositar" ))
    mi_cuenta.depositar(monto)
    
    retiro = int(input("Porfavor ingresa el monto a retirar "))
    mi_cuenta.retirar(retiro)
except ValueError:
    print("Porfavor ingresa un numero entero")



mi_cuenta.ver_balance()

class CuentaAhorros(CuentaBancaria):
    
    def aplicar_intereses(self):
        interes = self.balance *0.02
        self.balance += interes
        print(f"Se ha aplicadoun interes del 2%  {self.balance}")
        
mi_ahorro = CuentaAhorros()
mi_ahorro.depositar(1000)
mi_ahorro.aplicar_intereses()
mi_ahorro.ver_balance()