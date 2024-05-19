import itertools

def brute_force(charset, maxlength):
    """
    Esta función genera todas las posibles combinaciones de caracteres en un conjunto de caracteres hasta una longitud máxima.
    """
    return (''.join(candidate)
            for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
            for i in range(1, maxlength + 1)))

# Ejemplo de uso:
for attempt in brute_force('abc123', 2):
    print(attempt)
