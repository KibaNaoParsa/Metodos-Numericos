def bisseccao(funcao, a, b, tol=1e-6, k_max=100, mostrar=False):
	
	""" Refinamento de Raizes: Metodo da Bisseccao
	
		Requer:
			'funcao' seja continua em [a, b]
			'funcao(a) * funcao(b) < 0' -> isto e, quantidade impar de raizes
			
		Retorna:
			o zero da 'funcao' com o tol informado.
	"""
	
	fa = funcao(a)
	fb = funcao(b)
	if fa * fb >= 0:
		raise ValueError("Requer que: funcao(a) * funcao(b) < 0")
	
	if mostrar:
		titulo = "{:>3} | {:>12}, {:>12} | {:>12} | {:>14} | {:>14} | {:>14}"
		print(titulo.format("k", "a", "b", "X[k]", "f(X[k])", "f(a)", "b-a"))
	modelo = "{:3d} | [{:12.8f}, {:12.8f}] | {:12.8f} | {:+14.8f} | {:+14.8f} | {:14.8f}"
	fa = funcao(a)
	k = 1
	
	while k <= k_max:
		xk = (a + b) / 2.0
		fxk = funcao(xk)
		if mostrar:
			print(modelo.format(k, a, b, xk, fxk, fa, b-a))
		if b - a < tol and abs(fxk) < tol:
			break
		if fa * fxk < 0:
			b = xk
		else:
			a = xk
			fa = fxk
		k = k + 1
	return xk
