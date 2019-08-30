def newton(funcao, funcao_d, x0, tol=1e-6, k_max=100, mostrar=False):
    """Refinamento de Raizes: Metodo Newton

       Requer:
            'funcao_d' seja nao nula

       Retorna:
            o zero da 'funcao' com o tol informado
            (convergencia nao eh garantida)
    """

    k = 0
    xk = x0
    fxk = funcao(xk)
    delta_x = - funcao(xk) / funcao_d (xk)

    if mostrar:
        titulo = "{:>3} # {:>12} # {:>14} # {:>14}"
        print(titulo.format("k", "X[k]", "f(X[k])", "delta_x"))
        md = "{:3d} # {:12.8f} # {:+14.8f}"
        print(md.format(k, xk, fxk))

    modelo = "{:3d} # {:12.8f} # {:+14.8f} # {:14.8f}"

    k = 1
    while k <= k_max:
        xk = xk + delta_x
        fxk = funcao(xk)
        if mostrar:
            print(modelo.format(k, xk, fxk, delta_x))
        if abs(delta_x) < tol and abs(fxk) < tol:
            break
        try:
			delta_x = - fxk / funcao_d (xk)
        except:
			raise ValueError("Requer que: 'funcao_d' seja nao nula")
        k = k + 1
    return xk
