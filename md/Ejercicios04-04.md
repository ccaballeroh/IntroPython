```python
w = input("ingresa peso en kg: ")
h = input ("ingresa altura en m: ")
try:
    w = float(w)
    h = float(h)

    IMC = w/h**2
    print("IMC: ", IMC)

    if IMC < 18.5:
        print("Bajo peso")

    elif IMC >= 18.5 and IMC < 25:
        print("Normal")

    elif IMC >= 25 and IMC < 30:
        print("Sobrepeso")

    else:
        print("Obesidad")
  
except:
    print("ingresar solamente números")
    
input()
```