def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def suma_n(n):
    if n == 0:
        return 0
    return n + suma_n(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def contar_letra(palabra, letra, i=0):
    if i == len(palabra):
        return 0
    elif palabra[i] == letra:
        return 1 + contar_letra(palabra, letra, i + 1)
    else:
        return contar_letra(palabra, letra, i + 1)

def invertir_cadena(cadena):
    if cadena == "":
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Factorial")
        print("2. Suma de los primeros N números")
        print("3. Número n de Fibonacci")
        print("4. Contar letra en palabra")
        print("5. Invertir cadena")
        print("6. Potencia (base^exponente)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = input("Ingrese un número entero positivo: ")
            if n.isdigit():
                print("Resultado:", factorial(int(n)))
            else:
                print("Entrada inválida.")

        elif opcion == "2":
            n = input("Ingrese un número entero positivo: ")
            if n.isdigit():
                print("Resultado:", suma_n(int(n)))
            else:
                print("Entrada inválida.")

        elif opcion == "3":
            n = input("Ingrese un número entero positivo: ")
            if n.isdigit():
                print("Resultado:", fibonacci(int(n)))
            else:
                print("Entrada inválida.")

        elif opcion == "4":
            palabra = input("Ingrese una palabra: ")
            letra = input("Ingrese la letra a contar: ")
            if len(letra) == 1:
                print("Resultado:", contar_letra(palabra, letra))
            else:
                print("Debe ingresar solo una letra.")

        elif opcion == "5":
            cadena = input("Ingrese una cadena: ")
            print("Resultado:", invertir_cadena(cadena))

        elif opcion == "6":
            base = input("Ingrese la base: ")
            exponente = input("Ingrese el exponente entero positivo: ")
            if base.lstrip("-").isdigit() and exponente.isdigit():
                print("Resultado:", potencia(int(base), int(exponente)))
            else:
                print("Entrada inválida.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

menu()







