import random

print("Introduzca la longitud")
longitud = input()

cont = 0
cadena = ""

while cont < int(longitud):
    cadena += str(random.randint(0, 9))
    cont += 1
print(cadena)
print("Introduzca una cadena de numeros")
numUsuario = input()

while not numUsuario.__eq__(cadena):
    if len(numUsuario) != len(cadena):
        print("Has introducido una cadena de distinta longitud a la establecida antes")
    else:
        cont = 0
        aciertos = ""

        while cont < len(cadena):
            if cadena[cont] == numUsuario[cont]:
                aciertos += f" {cadena[cont]} "

            cont += 1

        if len(aciertos) != 0:
            print(f"Has acertado los números: {aciertos}")
        else:
            print("No has acertado ningún número")

    print("Introduzca una cadena de numeros")
    numUsuario = input()

print("Has acertado!")