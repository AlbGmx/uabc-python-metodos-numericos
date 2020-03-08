# Luis G. Diaz Reynoso 1260642
# Metodo Abierto - Newton Raphson 2do Orden

# IMPORTANTE: Instalar tabulate con 'pip install tabulate' https://pypi.org/project/tabulate/

from tabulate import tabulate
import math

# Ecuacion polinomial
def defineEcuacion():
    print("\n--------- Captura tu ecuacion polinomial ---------")
    orden = int(input("Orden de la ecuacion: "))
    c = 0
    while orden >= c:
        coef = float(input(f"Coeficiente del termino con orden x^{orden} : "))
        ec[0].append(orden)
        ec[1].append(coef)
        orden -= 1
    
    print("Tu ecuacion es: ")
    while len(ec[0]) > c:
        print(f"{ec[1][c]}x^{ec[0][c]} ", end="")
        if c != len(ec[0])-1:
            print("+ ", end="")
        c += 1
    print("\n")

def derivadaEcuacion1():
    c = 0
    while (len(ec[0])-1) > c:
        # Coeficiente Derivada = ExpEc * CoefEc
        ecD[0].append(ec[0][c+1])
        ecD[1].append(ec[0][c] * ec[1][c])
        c += 1

    i = 0
    print("Su primera derivada es: ")
    while len(ecD[0]) > i:
        print(f"{ecD[1][i]}x^{ecD[0][i]} ", end="")
        if i != len(ecD[0])-1:
            print("+ ", end="")
        i += 1
    print("\n")

def derivadaEcuacion2():
    c = 0
    while (len(ecD[0])-1) > c:
        # Coeficiente Derivada = ExpEc * CoefEc
        ecDD[0].append(ecD[0][c+1])
        ecDD[1].append(ecD[0][c] * ecD[1][c])
        c += 1

    i = 0
    print("Su segunda derivada es: ")
    while len(ecDD[0]) > i:
        print(f"{ecDD[1][i]}x^{ecDD[0][i]} ", end="")
        if i != len(ecDD[0])-1:
            print("+ ", end="")
        i += 1
    print("\n")


def newtonRaphson():
    nIteraciones = int(input("Número de iteraciones a realizar: "))
    xi = int(input("Valor de Xi (valor inicial): "))
    print("\n")

    # Iteraciones, Xi, f(Xi), f'(Xi), f''(Xi), Ea(error aprox.)
    table = [[] for x in range(nIteraciones)]
    msg = ""
    earlyExit = False
    ea = 0
    xia = xi

    for c in range(nIteraciones):
        fx = 0
        fxd = 0
        fxdd = 0

        # Resultado de sustituir xi en la funcion y derivada. (SOLO PARA POLINOMIOS).
        for i in range(len(ec[0])):
            fx += (xi**ec[0][i])*ec[1][i]
        for i in range(len(ecD[0])):
            fxd += (xi**ecD[0][i])*ecD[1][i]
        for i in range(len(ecDD[0])):
            fxdd += (xi**ecDD[0][i])*ecDD[1][i]

        table[c].append(c+1)
        table[c].append(xi)
        table[c].append(fx)
        table[c].append(fxd)
        table[c].append(fxdd)

        # Saca error porcentual
        if c > 0:
            ea = ((xi - xia)/xi)*100
            xia = xi
        table[c].append(ea)

        # Para sacar xi la division entre 0 no es valida.
        if ((fxd**2)-(fx*fxdd)) == 0:
            msg = "[f`(xi)^2 - f(xi)f``(xi)] = 0 // Divisor = 0 ::: Punto estacionario."
            earlyExit = True
            break

        xi = xi - ((fx*fxd) / ((fxd**2)-(fx*fxdd)))

        if ea == 0 and c > 0:
            msg = f"Tu raíz es: {xi:.30f}"
            earlyExit = True
            break
        
    print(tabulate(table, headers=['Iteración', 'xi', 'f(xi)', 'f`(xi)', 'f``(xi)', 'ea'], tablefmt="fancy_grid", floatfmt=".20f"))

    if (earlyExit):
        print(msg)
    elif c == nIteraciones:
        print("Iteraciones insuficientes o rango insuficiente. No se pudo llegar a la raíz.")
    else:
        print("Raíz imaginaria o inexistente.")
    print("\n")


# Exponentes [0] y coeficientes [1]
ec = [[], []]
ecD = [[], []]
ecDD = [[], []]
defineEcuacion()
derivadaEcuacion1()
derivadaEcuacion2()
newtonRaphson()