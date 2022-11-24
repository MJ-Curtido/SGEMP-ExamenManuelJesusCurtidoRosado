class Agenda:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def imprimirMenu(self):
        print("* Añadir contacto")
        print("* Lista de contactos")
        print("* Buscar contacto")
        print("* Editar contacto")
        print("* Cerrar Agenda")

print("¿Quieres introducir un contacto? (si/no)")
respuesta = input()

while respuesta.lower().__eq__("si"):
    print("Introduce el nombre")
    nombre = input()

    print("Introduce el teléfono")
    telefono = input()

    print("Introduce el email")
    email = input()

    contacto = Agenda(nombre, telefono, email)

    contacto.imprimirMenu()

    print("¿Quieres introducir un contacto? (si/no)")
    respuesta = input()