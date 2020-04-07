```python
try:
    w = float(input("ingresa peso en kg: "))
    assert w > 2 and w < 500, "El peso está fuera de rango"

    h = float(input("ingresa altura en m: "))
    assert h > 0.5 and h < 2.5, "Altura fuera de rango"

    IMC = w / (h ** 2)
    print("IMC: ", IMC)

    if IMC < 18.5:
        print("Bajo peso")
    elif IMC >= 18.5 and IMC < 25:
        print("Normal")
    elif IMC >= 25 and IMC < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")

except AssertionError as e:
    print(e)

except ValueError:
    print("ingresar solamente números")

input()
```