def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

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
    else palabra[i] == letra:
        return 1 + contar_letra(palabra, letra, i + 1)
    return contar_letra(palabra, letra, i + 1)

def invertir_cadena(cadena):
    if cadena == "":
        return ""
    elif:
        return invertir_cadena(cadena[1:]) + cadena[0]







