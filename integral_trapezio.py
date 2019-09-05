def g(x):
	return x**3 - x/2
	
def integral_trapezio(a, b, num_hs):
	h = (b - a) / num_hs
	soma = 0.0
	x = a
	i = 0
	while i <= num_hs:
		base = g(x)
		Base = g(x+h)
		area = h/2 * (Base + base)
		soma = soma + area
		i = i + 1
		x = x + h
	return soma
