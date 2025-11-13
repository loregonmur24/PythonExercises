# Importa el módulo json para trabajar con archivos JSON
import json

"""
Función: save_dates
Propósito: Guardar el diccionario de fechas en un archivo JSON
Parámetros:
  - dates: diccionario con nombres como clave y fechas como valor
"""
def save_dates(dates):
    # Abre el archivo en modo escritura ('w')
    with open('dates.json', 'w') as file:
        # Convierte el diccionario Python a formato JSON y lo guarda en el archivo
        json.dump(dates, file)

"""
Función: load_dates
Propósito: Cargar las fechas desde el archivo JSON
Retorna: 
  - Diccionario con las fechas si el archivo existe
  - Diccionario vacío {} si el archivo no existe (primera ejecución)
"""
def load_dates():
    try:
        # Intenta abrir el archivo en modo lectura ('r')
        with open('dates.json', 'r') as file:
            # Convierte el contenido JSON a un diccionario Python
            return json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, retorna un diccionario vacío
        return {}

"""
Función: add_date
Propósito: Agregar una nueva fecha al diccionario y guardarla permanentemente
Parámetros:
  - dates: diccionario actual de fechas
  - name: nombre de la persona
  - date: fecha a almacenar
"""
def add_date(dates, name, date):
    # Agrega o actualiza la fecha para el nombre dado en el diccionario
    dates[name] = date
    # Guarda los cambios en el archivo JSON
    save_dates(dates)
    # Confirma al usuario que la operación fue exitosa
    print(f"{name}'s date has been added.")

"""
Función: list_dates
Propósito: Mostrar todas las fechas almacenadas en el sistema
Parámetros:
  - dates: diccionario con todas las fechas
"""
def list_dates(dates):
    # Verifica si el diccionario tiene elementos
    if dates:
        print("List of Dates:")
        # Itera sobre cada par clave-valor en el diccionario
        for name, date in dates.items():
            # Muestra cada nombre y su fecha correspondiente
            print(f"{name}: {date}")
    else:
        # Mensaje si no hay fechas almacenadas
        print("No dates have been added.")

"""
Función: search_date
Propósito: Buscar y mostrar la fecha asociada a un nombre específico
Parámetros:
  - dates: diccionario con todas las fechas
  - name: nombre a buscar
"""
def search_date(dates, name):
    # Verifica si el nombre existe en el diccionario
    if name in dates:
        # Si existe, muestra la fecha asociada
        print(f"{name}'s date: {dates[name]}")
    else:
        # Si no existe, informa al usuario
        print(f"No date found for {name}.")

"""
Función: main
Propósito: Función principal que controla el flujo del programa
           y muestra el menú interactivo al usuario
"""
def main():
    # Carga las fechas existentes al iniciar el programa
    dates = load_dates()

    # Bucle infinito que mantiene el programa ejecutándose hasta que el usuario elija salir
    while True:
        # Muestra el menú de opciones
        print("\nOptions:")
        print("1. Add Date")
        print("2. List Dates")
        print("3. Search Date")
        print("4. Quit")

        # Solicita al usuario que ingrese su elección
        choice = input("Enter your choice: ")

        # Opción 1: Agregar una nueva fecha
        if choice == '1':
            name = input("Enter the person's name: ")
            date = input("Enter the date (e.g., YYYY-MM-DD): ")
            add_date(dates, name, date)

        # Opción 2: Listar todas las fechas almacenadas
        elif choice == '2':
            list_dates(dates)

        # Opción 3: Buscar una fecha específica por nombre
        elif choice == '3':
            name = input("Enter the person's name: ")
            search_date(dates, name)

        # Opción 4: Salir del programa
        elif choice == '4':
            print("Exiting program.")
            break  # Rompe el bucle while, terminando el programa

        # Maneja entradas inválidas
        else:
            print("Invalid choice. Please select a valid option.")

# Punto de entrada del programa - solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    main()

"""
ESTRUCTURA DE DATOS EJEMPLO:

El archivo dates.json almacena los datos en formato JSON:
{
    "Juan Pérez": "2024-01-15",
    "María García": "2024-02-20",
    "Carlos López": "2024-03-10"
}

FLUJO DEL PROGRAMA:
1. Al iniciar: Carga datos existentes desde dates.json
2. Durante ejecución: Mantiene datos en memoria (diccionario 'dates')
3. Al agregar/modificar: Guarda automáticamente en dates.json
4. Al finalizar: Los datos persisten para la próxima ejecución

CARACTERÍSTICAS:
- Persistencia de datos entre ejecuciones
- Manejo de errores (archivo no encontrado)
- Interfaz de usuario intuitiva
- Operaciones CRUD (Create, Read)
"""
