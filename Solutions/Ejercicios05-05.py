"""
Escribe un pequeño programa que cuente del 1 al 10,
pero que solo imprima los valores que no son múltiplos
de 2
"""
numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0:  # checa si es par
        continue
    print(numero)
input()
