import random

class JuegoEscaleras:
    def __init__(self):
        self.posicion = 0
        self.escaleras = 10
        
    def subir_escalera(self):
        if self.posicion < self.escaleras:
            self.posicion += 1
            print (f"Subiste un escalón. Estas en elescalon {self.posicion}. ")
        else:
            print (" Ya estas en el final de la escalera. ")
            
    def bajar_escalera(self):
        if self.posicion > 0:
            self.posicion -= 1
            print (f"Bajaste un escalón. Estas en elescalon {self.posicion}. ")
        else:
            print (" Ya estas en el inicio de la escalera. ")
            
    def jugar(self):
        while True:
            print ("\nOpciones: ")
            print("1. Subir escalera")
            print("2. Bajar escalera")
            print("3. Salir")
            opcion = input("Qué deseas hacer ")
            
            if opcion == "1":
                self.subir_escalera()
                if self.posicion == self.escaleras:
                    print("¡Felicitaciones! LLegaste al final de la escalera. ")
                    break
            elif opcion == "2":
                self.bajar_escalera()
            elif opcion == "3":
                print("Gracias por jugar. ")
                break
            else:
                print("Opcion invalida. intenta de nuevo.")
                
juego = JuegoEscaleras()
juego.jugar()
            
          