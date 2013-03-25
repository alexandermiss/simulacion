import os

def practica6():
    os.system('cls')
    print('Materia: Simulacion\t\tInstituto Tecnologico de Villahermosa\n \
	      \nCreado por: Alexander Miss \t Fecha: Mayo/2012\n\n')
    num=1.0
    aux=0.0
    iguales=0
    menores=0
    mayores=0
    totales=0
    for i in range(1,7):
	    for j in range(1,7):
		    print('(%s,%s)' % (j,i)),
		    aux = round((float(j) / float(i)),1)
		    auxr = round(aux,0)
		    if (auxr < num):
			    menores += 1
			    print('m: %s - %s' % (aux,auxr)),
		    elif (auxr > num):
			    mayores += 1
			    print('M: %s - %s' % (aux,auxr)),
		    else:
			    iguales += 1
			    print('i: %s - %s' % (aux,auxr)),
		    totales+=1
	    print('\n')
    print('Numero de totales\nMayores: %s \nMenores: %s \nIguales: %s' % ( \
	       mayores, menores, iguales))
    print('\n\nEstadisticas:\nMayores: %s%% \nMenores: %s%% \nIguales: %s%%' % ( \
	       round(float(mayores) / totales * 100,2), \
	       round(float(menores) / totales * 100,2), \
	       round(float(iguales) / totales * 100,2)))

def main():
        practica6()

if __name__ == "__main__":
    main()
