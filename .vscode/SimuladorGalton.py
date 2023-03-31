# Proyecto 3: Simulación de Máquina de Galton 
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5

from random import choice

def Simulación_Galton(c = 12 , n = 3000):
    base = c * [0]
    for bille in range(n):
        posicion = c // 2
        for clou in range(c-1):
            posicion += choice([-1,1])/2
        
        base[ int(posicion) ] += 1

    return base

def grafica( L ):
    M = max(L)
    for l in range( max(L) ):
        linea = ''
        for e in L:
            if e == M:
                linea += ' * '
                L[L.index(e)] -= 1
            else:
                linea += ' ' * 3
        print(linea)
        M -= 1

grafica( Simulación_Galton(n=50) )

