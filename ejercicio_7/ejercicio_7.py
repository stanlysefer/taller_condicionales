

# input

a = int(input("ingrese el valor de a en un numero entero: "))
b = int(input("ingrese el valor de b en un numero entero: "))
c = int(input("ingrese el valor de c en un numero entero: "))

# processing

p1=a+b
p2=a+c
p3=b+c

if p1==c:
    resultado=c, "es la suma de" ,a, "+" ,b
else:
    if p2==b:
        resultado=b, "es la suma de" ,a,"+",c,
    else:
        if p3==a:
            resultado=a, "es la suma de" ,b, "+" ,c
        else:
            resultado=("ninguna es suma de los otros dos")

# output

print(resultado)