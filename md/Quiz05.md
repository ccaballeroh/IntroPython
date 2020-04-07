# Quiz 5: 

1. ¿Cómo se le conoce en computación a *repetir*?

1. En tus propias palabras, ¿qué es un *algoritmo*?

1. Escribe con lápiz y papel la sintaxis para hacer un ciclo `while`.

1. Al final de la ejecución de este programa, ¿cuánto vale la variable `cont`?

    ```python
    cont = 10
    while cont > 0:
        print(cont)
        cont -= 1
    ```
    Inténtalo en la consola del intérprete de Python. Corre el bloque de código anterior y después imprime el valor de `cont` con `print(cont)`.
1. ¿Qué es un "ciclo infinito" y cómo podemos salir de él?
1. ¿Qué es una variable de bandera?
1. ¿Cuál es el uso de la palabra reservada `continue`?
1. Describe en palabras qué hace el siguiente programa y luego ejecútalo en la consola del intérprete de IPython (abre Anaconda prompt y escribe `ipython`).

    ```python
    numero = 0
    while numero < 100:
        numero += 1
        if numero % 3 != 0:
            continue
        print(numero)
    ```
