# Ejercicios de la sesión 5

**Instrucciones:** 

- En la misma carpeta `Ejercicios` que has estado usando. Escribe *scripts* con la ayuda de IDLE para resolver los ejercicios en clase. Recuerda ser consistente con la convención de nombres de tus ejercicios (v.g., `Ejercicios05-01.py`).

- Toma en cuenta que si quieres que tus ejercicios se puedan ejecutar haciendo doble clic en ellos, debes agregar una llamada a la función *built-in* `input()` para que no se cierre la ventana.

**Ejercicios:**

1. Implementa el algoritmo babilónico para calcular raíz cuadrada usando un ciclo `while`. El programa debe pedir al usuario un valor al cual calcular
la raíz cuadrada y un primer valor con cuál intentar. Al final debe imprimir el resultado junto con su cuadrado.

    ```
    > Ingresa un valor positivo al cuál calcular la raíz cuadrada: 26
    > Ingresa un primer valor aproximado: 5
    La solución es: 5.1 su cuadrado es: 26.00999999998
    ```

1. Modifica el programa anterior utilizando las instrucciones `try` y `except` junto con `assert` para **asegurarte** que el número al que se le va a calcular la raíz es positivo (mayor que cero) y que el primer intento no es cero.

    ```
    > Ingresa un valor positivo al cuál calcular la raíz cuadrada: -5
    El número ingresado no es positivo
    ```

    ```
    > Ingresa un valor positivo al cuál calcular la raíz cuadrada: 26
    > Ingresa un primer valor aproximado diferente de cero: 0
    El primer valor aproximado es cero
    ```



1. Modifica tu programa de IMC `Ejercicios04-05.py` de la sesión anterior para que se ejecute tres veces.


1. Modifica tu programa de IMC `Ejercicios04-05.py` de la sesión anterior para que se ejecute hasta que el usuario lo desee. Por ejemplo, que después de imprimir el resultado de IMC y categoría, le pregunte al usuario si desea salir.

    ```
    > Ingresa peso en kg: 65
    > Ingresa altura en m: 1.63
    IMC: 24.46460160160337235
    Normal
    'S' para salir: S
    ```

1. Escribe un pequeño programa que cuente del 1 al 10,
pero que solo imprima los valores que **no** son múltiplos
de 2. (Usa el operador módulo y la palabra reservada `continue`)