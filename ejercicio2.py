def pares_naturales(n):
    if n < 1 or n >= 10**6:
        return "n debe ser un número natural menor a 10^6."
    
    pares = []
    for a in range(1, n):
        b = n - a
        if b > 0:
            pares.append((a, b))
    return pares

print(pares_naturales(10**2))