print("      CATEGORIA       PRECIO      CODIGO      RECARGO/DIA DE ATRASO")
print("      Favoritos       $2.50         1                $0.50")
print("      Nuevos          $3.00         2                $0.75")
print("      Estrenos        $3.50         3                $1.00")
print("      Super estrenos  $4.00         4                $1.50")

print("\nIntroduzca el código de la categoría")
codigo = input()

print("\nIntroduzca los días de alquiler")
dia = input()

match codigo:
    case "1":
        print(f"Total a pagar: {2.5 + (float(dia) * 0.5)}")
    case "2":
        print(f"Total a pagar: {3 + (float(dia) * 0.75)}")
    case "3":
        print(f"Total a pagar: {3.5 + float(dia)}")
    case "4":
        print(f"Total a pagar: {4 + (float(dia) * 1.5)}")
    case _:
        print("Código incorrecto")