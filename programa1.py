'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
'''
num = int(input("Ingresa un número para sacar la factorial: "))

if num>=0:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial del {num} es: {factorial}")