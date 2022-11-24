class Triangulo:
    def __init__(self, lado1, lado2, lado3, angulo1, angulo2, angulo3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3

    def imprimirLadoMayor(self):
        lista = [self.lado1, self.lado2, self.lado3]

        lista.sort()

        print(f"Dimensión de lado/s mayor/es: {lista[len(lista) - 1]}")

    def imprimirTipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es un triángulo equilátero")
        else:
            if self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3:
                print("Es un triángulo escaleno")
            else:
                print("Es un triángulo isósceles")

triangulo1 = Triangulo(7, 7, 7, 60, 60, 60)
triangulo2 = Triangulo(7, 7, 4, 60, 60, 70)
triangulo3 = Triangulo(7, 5, 9, 90, 30, 60)

triangulo1.imprimirLadoMayor()
triangulo1.imprimirTipoTriangulo()
print("\n")
triangulo2.imprimirLadoMayor()
triangulo2.imprimirTipoTriangulo()
print("\n")
triangulo3.imprimirLadoMayor()
triangulo3.imprimirTipoTriangulo()
