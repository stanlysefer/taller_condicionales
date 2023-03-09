# input

CUOTA_FIJA=10000

gast_mensual=int(input("ingrese el gasto mensual del agua: "))

if gast_mensual <=50:
    costoagua_mensual=CUOTA_FIJA
else:
    if gast_mensual <= 200:
        costoagua_mensual=CUOTA_FIJA+2000*(gast_mensual-50)
    else:
        costoagua_mensual=CUOTA_FIJA+3000*(gast_mensual-50)


print(costoagua_mensual)