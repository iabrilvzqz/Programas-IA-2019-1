"""	Programa. Algoritmo de las k-medias
	Autores:	Vázquez Sánchez Ilse Abril """

import numpy as np

def distEuclidiana(muestras, medias):
	""" Esta función calcula la distancia euclidiana entre cada uno de los puntos que
	conforman las muestras y las medias """
	return list(np.linalg.norm(np.array(muestras) - np.array(medias), axis = 1))

def distMin(distancias):
	""" Esta función devuelve el índice del número menor de una lista """
	return np.argmin(np.array(distancias))

def distMax(distancias):
	""" Esta función devuelve el índice del número mayor de una lista """
	return np.argmax(np.array(distancias))

def media(puntos):
	""" Esta función obtiene las media de los puntos de un vector"""
	return list(np.mean(np.array(puntos), axis = 0))

def errorMedias(mediasAnt, mediasAct, k):
	""" Esta función determina la distancia entre las medias iniciales y las calculadas. En
	caso de haber diferencias entre ambas, devuelve True para continuar con los cálculos o, en
	caso contrario, False para indicar que el ciclo debe terminar"""
	for i in range(k):
		error = np.linalg.norm(np.array(mediasAnt[i]) - np.array(mediasAct[i]), None)
		if(error!=0):
			return True
	return False

def imprimirMedias(mediasAnt, mediasAct):
	""" Usamos la función mostrada a continuación para imprimir las medias obtenidas """
	print("Medias iniciales: ", mediasAnt)
	print("Medias finales: ", mediasAct)
	print('-' * 80)

def eligeMedias(m, k):
	""" Esta función se utiliza para seleccionar las medias con las cuales se llevará a cabo el algoritmo"""
	muestras = m.copy()
	medias = []
	dimension = len(muestras[0])
	# Calculamos la distancia al origen de los puntos de la muestra
	distancias = distEuclidiana(muestras, [0 for x in range(dimension)])
	# Elegimos como primera media el que está más cercano al origen 
	minimo = distMin(distancias)
	medias.append(muestras[minimo])
	# Calculamos la distancia de las muestras a la primera media seleccionada 
	distancias = distEuclidiana(muestras, medias)
	# Elegimos como k-1 medias restantes a los puntos que estén más alejados de la primera media seleccionada	
	for i in range(k-1):
		maxima = distMax(distancias)
		medias.append(muestras[maxima])
		muestras.pop(maxima)
	return medias

def kMedias(medias, muestras, k):
	""" Esta función se encarga de aplicar el algoritmo de las k medias """
	distancias, ptsMin = [], [[] for i in range(k)]
	pts = []
	error = True
	while(error):
		# Determinamos la distancia desde cada una de las medias a los puntos de las muestras
		for i in range(k):
			distancias.append(distEuclidiana(muestras, medias[i]))

		# Obtenemos los puntos que se utilizarán para obtener las nuevas medias según la distancia mínima obtenida
		for i in range(len(distancias[0])):
			for lista in distancias:
				pts.append(lista[i])

			# Determinamos a qué media los puntos calculados tienen una menor distancia
			minimo = distMin(pts)
			pts = []
			ptsMin[minimo].append(muestras[i])

		# Guardamos las medias antes de actualizarlas
		mediasAnt = medias.copy()
		
		# Obtenemos el nuevo valor de las medias
		for i in range(k):
			if ptsMin[i]:
				medias[i] = media(ptsMin[i])

		# Determinamos el error entre las medias
		error = errorMedias(mediasAnt, medias, k)
		distancias, ptsMin = [], [[] for i in range(k)]

		imprimirMedias(mediasAnt, medias)

k = 2	

muestras1 = [[8, 10], [3, 10.5], [7, 13.5], [5, 18], [5, 13], [6, 9], [9, 11], [3, 18], [8.5, 12], [8, 16]]
medias1 = eligeMedias(muestras1, k)
kMedias([[8, 10], [5,13]], muestras1, k)

muestras2 = [[1, 12.5], [3, 10.5], [3, 12.5], [3, 14.5], [3, 18], [5, 18], [5, 16], [5, 14.5], [5, 13], [6, 9], [8, 10], [9, 11], [8.5, 12], [7, 13.5], [8, 16], [0.5, 10.5]]
medias2 = eligeMedias(muestras2, k)
kMedias([[3,14.5], [9,11]], muestras2, k)

muestras3 = [[9,12], [1,12.5], [6,9], [3,10.5], [9,11], [3,18], [8,14],[5,13], [8,10], [0.5,10]]
medias3 = eligeMedias(muestras3, k)
kMedias(medias3, muestras3, k)