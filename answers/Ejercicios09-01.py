"""
Escribe un *script* en el que definas una clase llamada `Gato` con tres atributos: `nombre`,  `edad` y `vivo`.
Al momento de instanciarse un objeto, se le debe pasar únicamente un nombre ya que la edad deberá ser `0` y el atributo `vivo`
deberá ser `True`.

Implementa un método `cumplir_años` que incremente en `1` la edad y que al llegar a `15` cambie el atributo `vivo` a `False`. 

    ```python
    gatito = Gato("Garfield")
    while gatito.vivo:
        gatito.cumplir_años()
    print(gatito.edad, gatito.vivo, gatito.nombre)
    ```
"""


class Gato:
    def __init__(self, nombre):
        """Asigna un nombre a una instancia, asigna 0 a la `edad` y True a `vivo`"""
        self.nombre = nombre
        self.edad = 0
        self.vivo = True

    def cumplir_años(self):
        """Incrementa en uno la edad y cambia atributo `vivo` a False al rebasar 15 años"""
        self.edad += 1
        if self.edad > 15:
            self.vivo = False


gatito = Gato("Garfield")
while gatito.vivo:
    gatito.cumplir_años()
print(gatito.edad, gatito.vivo, gatito.nombre)
