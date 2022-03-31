
print("1.Piedra")
print("2.Papel")
print("3.Tijera")
opcion = int(input("¿Que elijes Persona 1?: "))
opcion2 = int(input("¿Que eliges Persona 2?"))


if opcion == 1:
    eligepersona = "piedra"
elif opcion == 2:
    eligepersona = "papel"
elif opcion == 3:
    eligepersona = "tijera"
print("Elije: ", eligepersona)

if opcion2 ==1:
    elijepc = "piedra"
elif opcion2 ==2: 
    elijepc = "papel"
elif opcion2 == 3:
    elijepc= "tijera"




if elijepc == "papel" and eligepersona == "piedra":
    print("Ganas persona 2, papel envuelve la piedra")
elif elijepc == "papel" and eligepersona == "tijera":
    print("Ganaste, Tijera corta papel")
elif elijepc == "tijera" and eligepersona == "piedra":
    print("Ganaste, Piedra pisa tijera")
if elijepc == "papel" and eligepersona == "piedra":
    print("perdiste, papel envulve piedra")
elif elijepc == "tijera" and eligepersona == "papel":
    print("perdiste, Tijera corta papel")
elif elijepc == "piedra" and eligepersona == "tijera":
    print("perdiste, Piedra pisa tijera")
elif elijepc == eligepersona:
    print("empate")