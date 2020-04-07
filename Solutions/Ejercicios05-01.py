"""
Implementa el algoritmo babilónico usando un ciclo while.
El programa debe pedir al usuario un valor al cual calcular
la raíz y un primer valor con cuál intentar.
Al final debe imprimir el resultado junto con su cuadrado.

"""

num = float(input("> Ingresa un valor positivo al cuál calcular la raíz cuadrada: "))
sol = float(input("> Ingresa un primer valor aproximado: "))

while abs(sol ** 2 - num) > 0.01:
    sol = (sol + num / sol) / 2
print("La solución es: ", sol, "su cuadrado es: ", sol ** 2)
