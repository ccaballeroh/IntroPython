```python
"""
Rescribe el ejercicio 05-04 usando dos funciones:
una llamada `calcular_IMC` y otra `categoria_IMC`.
La primera debe tomar como argumentos el peso en kg
y la altura en metros y regresar el IMC.
La segunda debe tomar como argumento el IMC y
regresar una cadena con la categoría
("bajo de peso", "Normal", "Sobrepeso" y "Obesidad").
Tu programa debe comportarse de la misma forma que el 05-04.
En otras palabras, el usuario no se habrá
dado cuenta que el código cambió.
"""


def calcular_IMC(peso, altura):
    return peso / (altura ** 2)


def categoria_IMC(IMC):
    if IMC < 18.5:
        categoria = "Bajo peso"
    elif IMC >= 18.5 and IMC < 25:
        categoria = "Normal"
    elif IMC >= 25 and IMC < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return categoria


while True:
    try:
        w = float(input("> Ingresa peso en kg: "))
        assert w > 2 and w < 500, "El peso está fuera de rango"

        h = float(input("> Ingresa altura en m: "))
        assert h > 0.5 and h < 2.5, "Altura fuera de rango"

        IMC = calcular_IMC(w, h)
        print("IMC: ", IMC)

        categoria = categoria_IMC(IMC)
        print(categoria)

    except AssertionError as e:
        print(e)

    except ValueError:
        print("Ingresar solamente números")

    respuesta = input("'S' para salir: ")
    if respuesta == "S":
        break
```