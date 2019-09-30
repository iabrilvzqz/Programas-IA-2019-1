"""	Programa 2. Evolución de un autómara celular unidimensional
	Autor:  Vázquez Sánchez Ilse Abril"""

def automataCelular(n, aut):
	"""Esta función recibe como primer parámetro, el número de iteraciones que se desean realizar sobre el autómata y, como
	segundo parámetro, el autómata sobre el que se trabajará, el cual debe encontrarse dentro de una lista y, su población inicial
	debe estar separada por comas y representada mediante '1' (vivo) y '0' (muerto).
	El algoritmo aplicado es muy fácil de entender pues, simplemente, se revisa elemento por elemento y, según las reglas de
	evolución de un autómata unidimensional, se determina si el elemento permanecerá en su estado actual o debe cambiar."""
	resultado = []
	iteracion = 1
	while(iteracion < n):
		resultado.append(aut)
		autAuxiliar = []
		for i in range(len(aut)):
			if i > 0 and i < len(aut)-1:
				if aut[i-1] == aut[i] and aut[i+1] == aut[i]:
					autAuxiliar.append(0)
				else:
					autAuxiliar.append(1)

			elif(i == 0):
				if aut[1] == aut[0]:
					autAuxiliar.append(0)
				else:
					autAuxiliar.append(1)

			elif(i == len(aut)-1):
				if aut[len(aut)-2] == aut[len(aut)-1]:
					autAuxiliar.append(0)
				else:
					autAuxiliar.append(1)
		
		aut = autAuxiliar[:]
		iteracion += 1

	return resultado

def main():
	"""En la función main, leemos desde consola el número de iteraciones que el usuario desde que se realicen, así como
	el autómata, el cual se ingresa mediante una cadena de '1' y '0' sin separación entre cada uno de los elementos.
	El resultado final es presentado mediante asteriscos y espacios, por ello, se creó un diccionario para realizar el intercambio
	de caracteres en la cadena, para que sea más agradable y fácil de entender para el usuario"""
	mapeo = {0:' ', 1:'*'}
	aut = [ int(e) for e in input("Automata: ")]
	numIter = int(input("Ingrese el número de iteraciones: "))
	
	d = automataCelular(numIter, aut)
	for i in d:
		print(''.join([mapeo[c] for c in i]))

main()