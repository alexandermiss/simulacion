Simulacion
==========
Incluyen los métodos congruencial mixto y otros.
------------------------

Aquí los métodos de simulación

Archivo practica6.py:

Elegimos un número que nos servirá para ésta operación y la variable se llamará num, quedando así num=1.0

Contiene instrucciones que simulan la caída de dos dados. El resultado de ellos se divide uno entre otro y
se redondea de acuerdo a una cifra decimal.
Como ésta es una practica elaborada en clases, se usan dos ciclos "for" con límite 6 (porque todos y cada dado tiene
ese límite), de acuerdo al orden de los ciclos for se calculan los redondeos.
Un ejemplo es: si un dado cae en 5 y otro en 3 se divide 5/3 = 1.666666. Como sólo requerimos de una cifra decimal,
tomamos 1.6, pero al ser 1.6 más cerca de 2 a redondearlo, lo incluímos en la variable "mayores" que es un contador
y que es mayor al número 1, sí, la variable num.  No se incluye su valor, no se incluye el valor 2, sólo se cuenta
incrementado los contadores para saber cuántos números son mayores, menores o iguales a la variable num.

De esa misma manera se hace con todos los números, si en un dado cae 1 y en otro 1 no se redondea porque su resultado
es una cifra exacta y como es igual a la variable num, entonces se incluye en iguales. Todos los valores que son menores
a 1 también se incluyen en el contado menores.

Al finalizar se muestran los resultados se muestran en números y en forma de estadística.

Como son dos dados, y contando que el ciclo for no repetira una misma caída de dados, los resultados serán 36 cifras.
