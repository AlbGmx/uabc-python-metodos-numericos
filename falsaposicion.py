# Luis G. Diaz Reynoso 1260642
# Metodo Falsa Posicion

from tabulate import tabulate
import math

nEc = int(input("\nNumero de ecuación a testear (1-3): "))
nIteraciones = int(input("Número de iteraciones a realizar: "))
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
print("\n")

def ec(nEc, x):
    if nEc == 1:
        return 4*(x**3) - 6*(x**2) + 7*x - 2.3
    elif nEc == 2:
        return (x**2) - 3*x + 12
    elif nEc == 3:
        return (x**3) - ((x**2)/2) - 3*x + 2

def falsaposicion(a, b):
    if (a == b):
        print("Limite inf. no puede ser igual a limite sup.")
    else:
        # Iteraciones, Xi(a), Xu(b), Xr(xs), Ea(error aprox.)
        table = [[] for x in range(nIteraciones)]
        c = 0
        raiz = False

        xs = 0
        ea = 0

        while c < nIteraciones:
            fa = ec(nEc, a)
            fb = ec(nEc, b)

            if xs != 0:
                ea = (((b - (fb*(a-b)/(fa-fb))) - xs) / ((b - (fb*(a-b)/(fa-fb))))) *100
            xs = b - (fb*(a-b)/(fa-fb))

            fxs = ec(nEc, xs)
            
            table[c].append(c+1)
            table[c].append(a)
            table[c].append(b)
            table[c].append(xs)
            table[c].append(f"{ea:.20f} %")
            
            c+=1

            if (fa*fxs) < 0:
                b = xs
            elif (fa*fxs) > 0:
                a = xs
            elif (fa*fxs) == 0 and c > 1:
                raiz = True
                break

            # Raiz imaginaria
            if abs(ea) == 0 and c > 1 and a != b:
                raiz = True
                break

            
        print(tabulate(table, headers=['Iteración', 'Xi', 'Xu', 'Xr', 'Ea'], tablefmt="fancy_grid", floatfmt=".30f"))

        if (raiz):
            print(f"Tu raíz es: {xs:.30f}")
        elif c == nIteraciones:
            print("Iteraciones insuficientes o rango insuficiente. No se pudo llegar a la raíz.")
        elif a == b:
            print("Raíz imaginaria o inexistente.")
        print("\n")

falsaposicion(a, b)