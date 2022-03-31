print("Digite tres números para calcular el mínimo")
valor1 = int(input("primer número: "))
valor2 = int(input("segundo número: "))
valor3 = int(input("tercer número: "))

if valor1 < valor2:
    if valor1 < valor3:
        minimo_valor = valor1
    else:
        minimo_valor = valor3
elif valor2 < valor3:
    minimo_valor = valor2
else:
    minimo_valor = valor3

print("El número mínimo es: ", minimo_valor)
