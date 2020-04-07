"""
Implementa el algoritmo babilónico para calcular raíz cuadrada
usando un ciclo while. El programa debe pedir al usuario
un valor al cual calcular la raíz y un primer valor con
cuál intentar. Al final debe imprimir el resultado
junto con su cuadrado.

Utiliza instrucciones `try` y `except` junto con `assert` para
*asegurarte* que el número al que se le va a calcular la
raíz es positivo (mayor que cero) y que el primer intento
no es cero. 
"""

try:
    num = float(
        input("> Ingresa un valor positivo al cuál calcular la raíz cuadrada: ")
    )
    assert num > 0.0, "El número ingresado no es positivo"

    sol = float(input("> Ingresa un primer valor aproximado diferente de cero: "))
    assert sol != 0, "El primer valor aproximado es cero"

    while abs(sol ** 2 - num) > 0.01:
        sol = (sol + num / sol) / 2

    print("La solución es: ", sol, "su cuadrado es: ", sol ** 2)
    input()

except AssertionError as e:
    print(e)
