def resolverSL_gauss(M, b, mostrar=False):
		""" Sistema linear: Metodo de Gauss
			
			M: Matriz dos coeficientes
			b: Lista dos termos independentes
			
			Requer que:
				Dimensoes de M seja nxn e de b seja n
				M seja uma matriz não singular
				
			Retorna:
				X: Solucao do sistema linear
		"""
		zerar_triangulo(M, b, mostrar)
		return resolverSL_TS(M, b)


def zerar_triangulo(M, b, mostrar=True):
	""" Zera os elementos abaixo da diagonal principal
		utilizando as operacoes L-elementares
	"""
	
	n = len(M)
	k = 0
	while k < n - 1:
		zerar_coluna_j(k, M, b)
		if mostrar:
			
		
		k = k + 1


def zerar_coluna_j(j, M, b):
	""" Zera os elementos da coluna j abaixo do pivo Mij
		utilizando as operacoes L-elementares 
	"""
	
	n = len(M)
	i = j + 1
	while i < n:
		zerar_Mij(i, j, M, b)
		i = j + 1


def zerar_Mij(i, j, M, b):
	"""  Zera o elemento Mij onde i > j 
		utitlizando as operacoes L-elementares
	"""
	
	n = len(M)
	i_pivo = j
	z = - M[i][j] / M[j][j]

	while j < n:
		M[i][j] = M[i][j] + z * M[i_pivo][j]
		j = j + 1
	b[i] = b[i] + z * b[i_pivo]


def resolverSL_TS(M, b):
	
	n = len(M)
	X = n * [0.0]
	i = n - 1
	while i >= 0:
		soma_i = 0.0
		j = i + 1
		while j < n:
			soma_i = soma_i + M[i][j] * X[j]
			j = j + 1
		X[i] = (b[i] - soma_i) / M[i][i]
		i = i - 1
	return X
	
	
def imprimir_matrizes(k, M, b):
	""" Imprime M|b """

	n = len(M)
	print("j = {:2d}".format(j))
	print("  M|b =")
	i = 0
	while i < n:
		j = 0
		while j < n:
			print("{:10.4f}".format(M[i][j]), end="")
			j = j + 1
		print("    | {:10.4f}".format(b[i]))
		i = i + 1
	print("")
