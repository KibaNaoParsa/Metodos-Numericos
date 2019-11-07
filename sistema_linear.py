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
	
