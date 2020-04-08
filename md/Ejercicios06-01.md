```python
"""
Reutiliza tu código del ejercicio 04-02, de cálculo de paga
por horas con tarifa más alta en horas extra, pero en lugar
de pedir al usuario el número de horas y la tarifa base,
imprime el resultado para tres casos diferentes en el mismo programa.
"""
# Primer caso
num_horas = 30.0
tarifa_base = 247.0

num_horas = float(num_horas)
tarifa_base = float(tarifa_base)

if num_horas > 40:
    horas_extra = num_horas - 40
    adicional = 1.5 * tarifa_base

    pago_normal = 40 * tarifa_base
    paga_extra = horas_extra * adicional

    paga_total = pago_normal + paga_extra
else:
    paga_total = num_horas * tarifa_base

print(f"El pago por {num_horas} horas a {tarifa_base} por hora es: {paga_total}")

# Segundo caso

num_horas = 47.0
tarifa_base = 311.0

num_horas = float(num_horas)
tarifa_base = float(tarifa_base)

if num_horas > 40:
    horas_extra = num_horas - 40
    adicional = 1.5 * tarifa_base

    pago_normal = 40 * tarifa_base
    paga_extra = horas_extra * adicional

    paga_total = pago_normal + paga_extra
else:
    paga_total = num_horas * tarifa_base

print(f"El pago por {num_horas} horas a {tarifa_base} por hora es: {paga_total}")

# Tercer caso

num_horas = 43.5
tarifa_base = 117.80

num_horas = float(num_horas)
tarifa_base = float(tarifa_base)

if num_horas > 40:
    horas_extra = num_horas - 40
    adicional = 1.5 * tarifa_base

    pago_normal = 40 * tarifa_base
    paga_extra = horas_extra * adicional

    paga_total = pago_normal + paga_extra
else:
    paga_total = num_horas * tarifa_base

print(f"El pago por {num_horas} horas a {tarifa_base} por hora es: {paga_total}")
```