"""	Programa. Perceptrón
	Autor: Vázquez Sánchez Ilse Abril """


def pPunto(x, w):
	"""Función que regresa el producto punto entre el vector
	de pesos w y el vector de entrada x """
	return sum(xi * wi for xi, wi in zip(x, w))

def funEsc(v, w, t):
	"""Función que regresa el resultado de la función escalón.
	Si el producto punto es mayor o igual al umbral, regresa 1
	Si el producto punto es menor al umbral, regresa -1 """
	escalon = {True: 1, False: -1}
	return escalon[pPunto(v, w) >= t]

def imprimePesos(w):
	"""Función que imprime los vectores de pesos calculados en la función perceptrón"""
	print("Pesos:")
	print(["%.4f" % wi for wi in w])
	print('-' * 35)

def perceptron(x, w, t, n, pa):
	""" Esta función recibe los siguientes parámetros:
		x: conjunto de aprendizaje que contiene tuplas con los vectores de pesos y las salidas esperadas
		w: pesos iniciales
		t: umbral
		n: tasa de aprendizaje """
	error = True
	while(error):
		error = False
		for vector, salida in x:
			# Obtenemos el valor de la función escalón dado por el producto punto entre los vectores
			g = funEsc(vector, w, t)
			# Determinamos si hay diferencia entre la salida esperada y la calculada
			e = salida - g
			if e != 0:
				error = True
				for i, xi in enumerate(vector):
					# Calculamos los nuevos valores del vector de pesos
					w[i] += n * e * xi
		if (pa != w):
			imprimePesos(w)
			pa = w.copy()
		else:
			imprimePesos(w)
			if(error == True):
				print("No converge")
			break

vectorEntradas = [((1, 0, 0, 0), 1), ((1, 0, 1, 0), 1), ((1, 1, 0, 1), 1), ((1, 0, 1, 1), 1), ((1, 1, 1, 1), -1) ]
pesos = [0, 0, 0, 0]
pa = pesos.copy()
theta = 0
eta = 0.1
perceptron(vectorEntradas, pesos, theta, eta, pa)
