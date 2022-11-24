print("PRECIOS\n")
print("CAMISA..................10€")
print("CINTURÓN................10€")
print("ZAPATOS.................10€")
print("PANTALON................10€")
print("CALCETINES..............10€")
print("FALDAS..................20€")
print("GORRAS..................20€")
print("SUETER..................20€")
print("CORBATA.................20€")
print("CHAQUETA................20€")
print("CÓDIGOS\n")
print("CAMISA..................1")
print("CINTURÓN................2")
print("ZAPATOS.................3")
print("PANTALON................4")
print("CALCETINES..............5")
print("FALDAS..................6")
print("GORRAS..................7")
print("SUETER..................8")
print("CORBATA.................9")
print("CHAQUETA................10")
print("\n")

print("Introduzca un código de la prenda que quieres comprar")
codigo = input()

print("Introduzca el número de esa prenda que quieres comprar")
num = input()

match codigo:
    case "1":
        print(f"Precio total {10 * int(num)}€")
    case "2":
        print(f"Precio total {10 * int(num)}€")
    case "3":
        print(f"Precio total {10 * int(num)}€")
    case "4":
        print(f"Precio total {10 * int(num)}€")
    case "5":
        print(f"Precio total {10 * int(num)}€")
    case "6":
        print(f"Precio total {20 * int(num)}€")
    case "7":
        print(f"Precio total {20 * int(num)}€")
    case "8":
        print(f"Precio total {20 * int(num)}€")
    case "9":
        print(f"Precio total {20 * int(num)}€")
    case "10":
        print(f"Precio total {20 * int(num)}€")
    case _:
        print("Código incorrecto")