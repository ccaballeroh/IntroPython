"""
Escribe un programa que le pida continuamente
al usuario por tres números
(llamémoslos `x`, `y` y `z`) y despúes
los imprima en pantalla separados por una coma
y con dos saltos de línea al final.
El programa debe funcionar así:

    ```
    > Ingresa el valor de x: 30.5
    > Ingresa el valor de y: 17.9
    > Ingresa el valor de z: 29.7
    30.5,17.9,29.7

    > Ingresa el valor de x: 43.7
    > Ingresa el valor de y: 35.5
    > Ingresa el valor de z: 78.3
    43.7,35.5,78.3

    > Ingresa el valor de x: Ctrl-c
    Saliendo...
    ```
    """

while True:
    try:
        x = input("Ingresa el valor de x: ")
        y = input("Ingresa el valor de y: ")
        z = input("Ingresa el valor de z: ")
    except KeyboardInterrupt:
        print("\nSaliendo...")
        break

    print(x, y, x, sep=",", end="\n\n")
input()
