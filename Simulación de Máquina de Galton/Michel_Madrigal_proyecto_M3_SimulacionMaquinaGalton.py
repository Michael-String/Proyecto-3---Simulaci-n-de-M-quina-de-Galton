# Proyecto 3: Simulación de Máquina de Galton
# UCamper: Michel Amir Madrigal Torres
# Bootcamp: Fundamentos de Python
# Coach: Gustavo Mota
# Grupo: C5

#/// Primero representaremos en modo texto la lista obtenida con una simulación del lanzamiento de 
# 3000 canicas en 12 obstáculos.///

from random import choice

def Simulación_Galton(c = 12 , n = 3000):
    base = c * [0]
    for canica in range(n):
        posición = c // 2
        for obstaculo in range(c-1):
            posición += choice([-1,1])/2
        
        base[ int(posición) ] += 1

    return base

def gráfica( L ):
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

gráfica( Simulación_Galton(n=3000) )


# Si queremos una representación más elegante, podemos por ejemplo agregar la siguiente función de Python:

def graph_plot( L ):
    from numpy import arange
    from matplotlib.pyplot import bar, show
    c = len( L )
    x = arange(0,c,1)
    bar(x,L,width=0.8,color='red',alpha=0.5)
    show()
    
    # Lo que da, ejecutando:

graph_plot( Simulación_Galton(c = 12, n=3000) )



    
    

    
    
    