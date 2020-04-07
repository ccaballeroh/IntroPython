celsius = input("Ingresar temperatura en Celsius: ")
try:
    celsius = float(celsius)
    print("Fahrenheit:", 1.8*celsius + 32)
    input()
except:
    print("No mames, con número")
    input()
    
    
