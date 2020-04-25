from MisClases import Punto


def lanzar_puntos(*, n):
    """n puntos al azar en el cuadro unitario.
    
    Lanza n puntos al azar en el cuadro unitario y lleva
    la cuenta de la cantidad que caen dentro de un cuarto
    de círculo unitario.
    
    Entrada
    n: int - número de puntos
    
    Salida
    dentro: int - número de puntos a menos de 1 de distancia
    """
    contador = 0
    dentro = 0
    while contador < n:
        p = Punto()
        if p.dist < 1:
            dentro += 1
        contador += 1
    return dentro


def aproximar_pi(*, n):
    """Aproxima pi después de lanzar n puntos en el cuadro unitario.
    
    Pi es aproximadamente 4 veces la razón de puntos dentro de un cuarto de
    círculo unitario entre el total de puntos lanzados en un cuadrado unitario.
    
    Entrada
    n: int - número de puntos
    
    Salida
    aproximación de pi
    """
    return 4 * lanzar_puntos(n=n) / n


def correr_experimento(*, veces, n):
    """Promedio de aproximar_pi `veces` veces con `n` puntos."""
    cont = 0
    acum = 0
    while cont < veces:
        cont += 1
        acum += aproximar_pi(n=n)
    return acum / veces


pi = correr_experimento(veces=1000, n=1000)

print(f"pi se aproxima a {pi:.5f}")
