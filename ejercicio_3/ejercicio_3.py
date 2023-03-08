#programa que le indique el precio de ventade un articulo dado.
# input

p = int(input("ingrese el costo del articulo: "))

# processing

if p < 3000:
    ganancia = p*0.15
    pre_ven=p+ganancia
else:
    if p<=6000: 
        ganancia=500
        pre_ven=p+ganancia
    else:
        ganancia=p*0.25
        pre_ven=p+ganancia
        

# output

print("el costo es: " + str(pre_ven))