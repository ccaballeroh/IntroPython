# Ejercicios de la sesión 9

**Instrucciones:**
En tu carpeta `Ejercicios` realiza lo siguiente:

1. Escribe un *script* en el que definas una clase llamada `Gato` con tres atributos: `nombre`,  `edad` y `vivo`. Al momento de instanciarse un objeto, se le debe pasar únicamente un nombre ya que la edad deberá ser `0` y el atributo `vivo` deberá ser `True`. Implementa un método `cumplir_años` que incremente en `1` la edad y que al llegar a `15` cambie el atributo `vivo` a `False`. 

    ```python
    gatito = Gato("Garfield")
    while gatito.vivo:
        gatito.cumplir_años()
    print(gatito.edad)
    ```


2. Define una clase llamada `Punto` con tres atributos, `x`, `y` y `dist`. Al momento de crear una instancia de esta clase debe asignarse al azar un número en el intervalo [0,1) y el atributo `dist` será la distancia euclidiana al origen [`(x**2 + y**2)**.5`]. **NOTA:** al inicio de tu archivo escribe lo siguiente para tener disponible una función llamada `random` que regresa un número en el intervalo [0,1).

    ```python
    from random import random
    ```
