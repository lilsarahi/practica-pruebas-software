def _validar(a, b):
    for x in (a, b):
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("Los argumentos deben ser numéricos")

def sumar(a, b):
    _validar(a, b)
    return a + b

def restar(a, b):
    _validar(a, b)
    return a - b

def multiplicar(a, b):
    _validar(a, b)
    return a * b

def dividir(a, b):
    _validar(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b