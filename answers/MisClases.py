"""
Clase que crea un punto con coordenadas `x` y `y` al azar en el intervalo [0,1).
Al momento de instanciarse, se asigna el atributo `dist` con la distancia euclidiana
desde el origen.
"""

from random import random


class Punto:
    def __init__(self):
        self.x = random()
        self.y = random()
        self.dist = (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self):
        return f"El punto P({self.x:.3f},{self.y:.3f}) está a una distancia {self.dist:.3f} del origen."


if __name__ == "__main__":
    p = Punto()
    print(p)
