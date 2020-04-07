número_horas = input("Ingresa número de horas: ")
tarifa = input ("Ingresa tarifa por hora: ")
try:
    número_horas = float(número_horas)
    tarifa = float(tarifa)

    if número_horas > 40:
        horas_extra = número_horas - 40
        adicional = 1.5 * tarifa

        pago_normal = 40 * tarifa
        paga_extra = horas_extra * adicional

        paga_total = pago_normal + paga_extra
    else:
        paga_total = número_horas * tarifa

    print("Paga:" , paga_total)
    input()

except:
    print("Error, ingresa un valor numérico")
    
