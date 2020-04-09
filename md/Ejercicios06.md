# Ejercicios de la sesión 6

**Instrucciones:** 

- En la misma carpeta `Ejercicios` que has estado usando. Escribe *scripts* con la ayuda de IDLE para resolver los ejercicios en clase. Recuerda ser consistente con la convención de nombres de tus ejercicios (v.g., `Ejercicios06-01.py`).

- Toma en cuenta que si quieres que tus ejercicios se puedan ejecutar haciendo doble clic en ellos, debes agregar una llamada a la función *built-in* `input()` para que no se cierre la ventana.

**Ejercicios:**

1. Reutiliza tu código de `Ejercicios04-02.py`, de cálculo de paga por horas con tarifa más alta en horas extra, pero en lugar de pedir al usuario el número de horas y la tarifa base, imprime el resultado para tres casos diferentes en el mismo programa. Los casos son:
    - 30 horas a 247 por hora
    - 47 horas a 311 por hora
    - 43.5 horas a 117.80 por hora

    ```
    El pago por 30.0 horas a 247.0 por hora es: 7410.0
    El pago por 47.0 horas a 311.0 por hora es: 15705.5
    El pago por 43.5 horas a 117.8 por hora es: 5330.45
    ```

    Ver [solución](./Ejercicios06-01.md)

1. Escribe una función `repetir_mensaje` que imprima un `mensaje` un número `n` de veces y **regrese** una cadena que diga "listo". La función debe comportarse así:
    
    ```python
    >> mensaje = "Hola"
    >> n = 3
    >> resultado = repetir_mensaje(mensaje, n)
    Hola
    Hola
    Hola
    >> print(resultado)
    listo
    ```

    Ver [solución](./Ejercicios06-02.md)

1. Utiliza el código del ejercicio 1 de esta sesión para hacer una función y mándala a llamar con los casos enumerados en el mismo ejercicio.

    Ver [solución](./Ejercicios06-03.md)

1. Rescribe el ejercicio 05-04 usando dos funciones: una llamada `calcular_IMC` y otra `categoria_IMC`. La primera debe tomar como argumentos el peso en kg y la altura en metros y regresar el IMC. La segunda debe tomar como argumento el IMC y regresar una cadena con la categoría ("Bajo de peso", "Normal", "Sobrepeso" y "Obesidad"). Tu programa debe comportarse de la misma forma que el 05-04. En otras palabras, el usuario no se habrá dado cuenta que el código cambió.

    Ver [solución](./Ejercicios06-04.md)

