list_num = [1,8,15,7,6,8,12,54] # Lista de los numeros a usar
 
def reduce_list(numbers):
    numbers = list(set(numbers)) # quito duplicados
    numbers.sort() #  Ordeno los numeros
    numbers.pop(-1) # quito el ultimo o mayor
    return numbers
 
def average(numbers):
    valor_medio = sum(numbers)/len(numbers)
    return valor_medio

checked_list=reduce_list(list_num) # verifica la lista y la ordena
average_number=average(checked_list) # calcula el promedio
print(average_number) # muestra el resultaado