#MENU DE PY CON WHILE TRUE

while True:
    print()
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4.SALIR")
    print()

    try:
        opcion = int(input("Opcion: "))
    except:
        opcion > 0 or opcion > 4   

    if opcion == 1 :
        print("1. SUMAR")

    elif opcion == 2 :
        print("2. RESTAR")

    elif opcion == 3 :
        print("3. MULTIPLICAR")

    elif opcion == 4 :
        break

    else:
        print("Opcion incorrecta")

print("\n Fin del programa")        