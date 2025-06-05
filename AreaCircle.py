import math

def area_circulo(radio):
  """Calcula el área de un círculo dado su radio.

  Args:
    radio: El radio del círculo.

  Returns:
    El área del círculo.
  """
  area = math.pi * radio**2
  return area

resultado = area_circulo(5)
print(resultado)  # Imprime 78.53981633974483