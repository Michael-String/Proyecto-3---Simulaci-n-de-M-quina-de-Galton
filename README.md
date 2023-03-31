# Proyecto-3---Simulacion-de-Maquina-de-Galton

El programa fue muy interesante de desarrollar pues reafirme los conocimientos adquiridos en el Módulo 3:

a) Primero, importé la función de elección del módulo aleatorio. Más adelante veremos por qué es interesante.

b) Establecí el número de obstáculos 12 (c = 12). Los obstáculos son los lugares que reciben las canicas al final. Tiene que ser un número par.

c) A continuación, defino una lista llamada base que inicialmente es [0,0,0,0,0,0,0] (c elementos nulos). Los elementos de esta lista representarán el número de canicas que terminarán en cada una de los obstáculos.

d) En la línea 6, inicializo un bucle iterativo para simular 3000 lanzamientos de canicas.

e) Para cada simulación de lanzamientos, fijo la posición inicial de la canica: en el medio (c//2).

f) Entonces asumo que hay c – 1 líneas de obstáculos (que siempre es el caso), así que simulo el encuentro de c – 1 obstáculos. Para cada uno de ellos, elijo al azar una dirección. Aquí estoy usando la opción ([-1,1]) para elegir entre "-1" y "1". Si sale "-1", la posición actual se reduce en 0,5; de lo contrario, se incrementa en 0,5.

g) Al final del ciclo iterativo en “obstáculo”, obtengo la posición de la canica (entre 0 y c-1). Entonces solo tengo que incrementar el valor ya contenido en la lista base para esta posición (líneas 11 y 12).
