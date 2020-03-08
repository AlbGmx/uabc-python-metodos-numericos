import math

a = float(input("\nDame el valor de a: "))
b = float(input("\nDame el valor de b: "))
c = float(input("\nDame el valor de c: "))

if a == 0:
    if b != 0:
        r1 = -c/b
        print(f'El resultado es una ec. lineal con raiz real: {r1}')
    else:
        print(f'Solución trivial')
else:
    discr = (b**2) - (4*a*c)
    if discr >= 0:
        r1 = (-b + math.sqrt(discr))/(2*a)
        r2 = (-b - math.sqrt(discr))/(2*a)
        print(f'El resultado son dos raíces reales: {r1} , {r2}')
    else:
        r1 = -b/(2*a)
        r2 = r1
        i1 = math.sqrt(abs(discr))/(2*a)
        i2 = -i1
        print(f'El resultado son dos raíces complejas: ({r1}, i{i1}), ({r2}, i{i2})')