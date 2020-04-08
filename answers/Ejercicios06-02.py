"""
Escribe una función `repetir_mensaje`
que imprima un `mensaje` un número `n`
de veces y **regrese** una cadena que
diga "listo". La función debe comportarse así:

    >> mensaje = "Hola"
    >> n = 3
    >> resultado = repetir_mensaje(mensaje, n)
    Hola
    Hola
    Hola
    >> print(resultado)
    listo
"""


def repetir_mensaje(mensaje, n):
    contador = 0
    while contador < n:
        print(mensaje)
        contador += 1
    return "listo"
