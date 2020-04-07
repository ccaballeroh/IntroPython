```python
"""
Modifica tu programa de IMC Ejercicios04-05.py de la sesión anterior
para que se ejecute hasta que el usuario lo desee. Por ejemplo, que
después de imprimir el resultado de IMC y categoría, le pregunte al
usuario si desea salir.
"""

while True:
    try:
        w = float(input("> Ingresa peso en kg: "))
        assert w > 2 and w < 500, "El peso está fuera de rango"

        h = float(input("> Ingresa altura en m: "))
        assert h > 0.5 and h < 2.5, "Altura fuera de rango"

        IMC = w / (h ** 2)
        print("IMC: ", IMC)

        if IMC < 18.5:
            print("Bajo peso")
        elif IMC >= 18.5 and IMC < 25:
            print("Normal")
        elif IMC >= 25 and IMC < 30:
            print("Sobrepeso")
        else:
            print("Obesidad")

    except AssertionError as e:
        print(e)

    except ValueError:
        print("Ingresar solamente números")

    respuesta = input("'S' para salir: ")
    if respuesta == "S":
        break
```