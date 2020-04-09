"""
Este programa le pide al usuario que ingrese valores de peso
en kilogramos y altura en metros para calcular el índice de
masa corporal (IMC) y la categoría a la que pertenece la
persona con esos valores de peso y altura. El programa
sigue pidiéndole al usuario por nuevos valores hasta que
presiona "S" para salir. Además, el programa verifica que solo
se ingresen números en rangos válidos de peso y altura. Para
el peso el rango es de 2 a 500 kg y de altura de 0.5 a 2.5
metros.
"""


def calcular_IMC(peso, altura):
    """Calcula IMC dados peso y altura.

    El índice de masa corporal se calcula
    al dividir el peso en kg por la altura al cuadrado
    en metros.

    Entradas:
    peso: un número
    altura: un número

    Regresa:
    un número flotante con el IMC
    """
    imc = peso / (altura ** 2)
    return imc


def categoria_IMC(IMC):
    """Calcula la categoría de peso dado el IMC.

    La categoría se estima por el rango en el que cae
    el IMC. Menor a 18.5 se tiene bajo peso. Entre 18.5
    y 25 el peso es normal. Entre 25 y 30 se tiene
    sobrepeso y más allá de 30 se tiene obesidad.

    Entradas:
    IMC: un número flotante

    Regresa:
    categoría: una cadena con la categoría de peso
    """
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
