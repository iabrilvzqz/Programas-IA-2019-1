"""	Programa. Algoritmo para obtener la tabla de verdad de funciones lógicas 
	Autores:	Vázquez Sánchez Ilse Abril """
def polacaInversa(fp):
	polInv, elem = [], []
	op_log = ['v', '^', '=>', '!', '<=>']
	expr = fp.split()
	for e in expr:
		if (e in op_log) or (e == '('): elem.append(e)
		elif e == ')':
			op = elem.pop()
			while op != '(':
				polInv.append(op)
				op = elem.pop()
		else: polInv.append(e)
	while len(elem) > 0:
		polInv.append(elem.pop())
	return polInv

def ev(fp, epa, dicUna, dicBin, pa):
		if len(fp) == 0:
			return pa

		e = fp[0]

		if e in dicBin:
			oi, od = pa.pop(), pa.pop()
			if e == '=>':
				pa = (ev([od, '!' , oi, 'v'], epa, dicUna, dicBin, pa))

			elif e == '<=>':	
				pa = (ev([od, oi, '=>', oi, od, '=>', ''], epa, dicUna, dicBin, pa))

			else:	
				pa.append(eval( str(od) + dicBin[e] + str(oi) ))
				
			return ev(fp[1:], epa, dicUna, dicBin, pa)

		elif e in dicUna:
			od = pa.pop()
			pa.append(eval(dicUna[e] + str(od)))
			return ev(fp[1:], epa, dicUna, dicBin, pa)	

		else:
			pa.append(e)
			return ev(fp[1:], epa, dicUna, dicBin, pa)

def tdd(f, fp, e, r):
	e['True'] = True
	e['False'] = False

	dicUna = {'!': 'not '}
	dicBin = {'v': ' or ', '^':' and ', '=>': '', '<=>': ''}

	return f(polacaInversa(fp), e, dicUna, dicBin, [])[0] == r


print('******** TDD ********')
# Función de prueba
fp1 = "( p => q ) => ( ( p ^ r ) => ( q ^ r ) )"

# Generamos todas las combinaciones posibles de valores para p y q
for p in[True, False]:
	for q in [True, False]:
		for r in [True, False]:
			print(tdd(ev, fp1, {'p': p, 'q': q, 'r': r}, True))