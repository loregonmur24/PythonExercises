# Importa el módulo random para generar números aleatorios
import random
 
"""
Función: roll_dice
Propósito: Simular el lanzamiento de dos dados de 6 caras
Retorna: Una tupla con dos números aleatorios entre 1 y 6
"""
def roll_dice():
    # random.randint(1,6) genera un número entero aleatorio entre 1 y 6 (ambos incluidos)
    return random.randint(1,6), random.randint(1,6)
 
"""
Función: check_roll
Propósito: Evaluar el resultado de la tirada de dados y clasificarlo
Parámetros:
  - dice1: valor del primer dado (1-6)
  - dice2: valor del segundo dado (1-6)
Retorna: Un mensaje string que clasifica el resultado según la suma
"""
def check_roll(dice1, dice2):
    # Calcula la suma de los valores de ambos dados
    sum_dices = dice1 + dice2
    
    # Evalúa el resultado basado en la suma total:
    # Caso 1: Suma baja (2-6) - Resultado desfavorable
    if sum_dices <= 6:
        return f"La suma de tus dados es {sum_dices}. Lamentable"
    
    # Caso 2: Suma media (7-9) - Resultado prometedor
    elif sum_dices > 6 and sum_dices < 10:
        return f"La suma de tus dados es {sum_dices}. Tienes buenas chances"
    
    # Caso 3: Suma alta (10-12) - Resultado excelente
    else:
        return f"La suma de tus dados es {sum_dices}. Parece una jugada ganadora"
    
    
# === PROGRAMA PRINCIPAL ===

# Llama a la función roll_dice() y desempaqueta la tupla en dos variables
num1, num2 = roll_dice()

# Evalúa el resultado de la tirada usando la función check_roll
result = check_roll(num1, num2)

# Muestra el resultado en la consola
print(result)

"""
EJEMPLOS DE EJECUCIÓN:

Caso 1: Si los dados salen 2 y 3 (suma = 5)
Salida: "La suma de tus dados es 5. Lamentable"

Caso 2: Si los dados salen 4 y 4 (suma = 8)  
Salida: "La suma de tus dados es 8. Tienes buenas chances"

Caso 3: Si los dados salen 6 y 5 (suma = 11)
Salida: "La suma de tus dados es 11. Parece una jugada ganadora"
"""
