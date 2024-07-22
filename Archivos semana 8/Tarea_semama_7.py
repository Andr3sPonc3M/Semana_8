# Tarea semana 7.
# Implementación de Constructores y Destructores en Python.

# Definición de la clase persona
class Persona:

    # Constructor de la clase persona
    def __init__(self, nombre, edad):

        # Se inicia los atributos de la persona
        self.nombre = nombre
        self.edad = edad
        # Mensaje de inicialización
        print(f"Se ha creado un objeto Persona con el nombre: {self.nombre} y la edad: {self.edad}")

    # Destructor de la clase persona
    def __del__(self):
        # Mensaje de destrucción
        print(f"El objeto Persona: {self.nombre} ha sido destruido")

# Definición de la clase Coche
class Coche:

    # Constructor de la clase Coche
    def __init__(self, marca, modelo):

        # Inicializa los atributos del objeto
        self.marca = marca
        self.modelo = modelo
        # Mensaje de inicialización
        print(f"Se ha creado un objeto Coche con la marca: {self.marca} y el modelo: {self.modelo}")

    # Destructor de la clase Coche
    def __del__(self):
        # Mensaje de destrucción
        print(f"El objeto Coche: {self.marca} {self.modelo} ha sido destruido")

# Creación de objetos
persona1 = Persona("Andrés", 38)
coche1 = Coche("Fiat", "Uno Vivace")

# Eliminación de objetos
del persona1
del coche1

# Fin del programa.

# Andrés Ponce M.

