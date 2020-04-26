```python
"""
Define una clase llamada `Punto` con tres atributos, `x`, `y` y `dist`.
Al momento de crear una instancia de esta clase debe asignarse al azar
un número en el intervalo [0,1) y el atributo `dist` será la distancia
euclidiana al origen [`(x**2 + y**2)**.5`].

**NOTA:** al inicio de tu archivo escribe lo siguiente para tener
disponible una función llamada `random` que regresa un número en el intervalo [0,1).

Define el método `__repr__` de tal forma que tengas una *interfaz* así con el obteto:

>> p = Punto()
>> print(p)
El punto P(0.357,0.942) está a una distancia 1.008 del origen.
"""

from random import random


class Punto:
    def __init__(self):
        self.x = random()
        self.y = random()
        self.dist = (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"El punto P({self.x:.3f},{self.y:.3f}) está a una distancia {self.dist:.3f} del origen."


p = Punto()
print(p)
```