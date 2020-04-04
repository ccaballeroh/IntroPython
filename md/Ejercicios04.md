# Ejercicios de la sesión 4

**Instrucciones:** 

- En la misma carpeta `Ejercicios` que creaste la sesión anterior, usando IDLE escribe *scripts*
para resolver las siguientes tareas. Sé consistente con la convención de nombres de tus ejercicios (v.g., `Ejercicios04-01.py`)


**Ejercicios:**

1. Vuelve a escribir tu programa para cálculo de paga para que el empleado reciba 1.5 veces la tarifa por hora para el tiempo
trabajado en exceso de 40 horas.
	
	`Ingresa número de horas: 45 `
	
	`Ingresa tarifa por hora: 10`
	
	`Paga: 475.0`

1. Modifica el mismo programa usando `try` y `except` para que tu programa pueda manejar el que se ingresen valores no numéricos
imprimiendo un mensaje y saliendo del programa. Por ejemplo:

	`Ingresa número de horas: 20`
	
	`Ingresa tarifa por hora: nueve`
	
	`Error, ingresa un valor numérico`
	
	
	`Ingresa número de horas: cuarenta`
	
	`Error, ingresa un valor numérico`


1. Escribe un programa que le pida al usuario su peso ($W$) en `kg` y su altura ($H$) en `m` y que imprima al usuario su IMC (índice de masa corporal) junto con la categoría
(bajo de peso, normal, sobrepeso, obesidad) guiándote con la siguiente tabla. ($IMC = \frac{W}{H^2}$).

|              **IMC**               | **Categoría** | 
|:-----------------------------------|:--------------|
| menor a 18.5                       | Bajo de peso  |
| mayor o igual a 18.5 y menor a 25  |    Normal     |
| mayor o igual a  25 y menor a 30   |   Sobrepeso   |
| mayor o igual 30                   |   Obesidad    |


1. Modifica tu programa anterior usando `assert` para que el programa garantice que el peso es mayor a 2 kg y menor a 500 kg y que la altura es mayor a medio metro y menor a 2.5 metros.