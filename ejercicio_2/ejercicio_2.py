#programa para realizar un prestamo bancario

print("------------------------------------------")
print("---El resultado de las operaciones son:---")
print("------------------------------------------")
#input
ingresos = int(input("Ingrese su ingreso mensual: "))

#processing
if ingresos > 945200:
    deudas = int(input("Ingrese el total de sus deudas: "))
    if deudas == 0:
        print("su prestamo a sido aceptado")
    else:
        print("su prestamo no ha sido aceptado")
else:
    print("su prestamo no a sido aceptado")

#output
print("print")