p1 = input().split(" ")

a, b, c = p1
pi = 3.14159
a = float(a)
b = float(b)
c = float(c)

TRIANGULO = a*c*.5
CIRCULO_1 = c**2
CIRCULO = CIRCULO_1 * pi
TRAPEZIO_1 = (a+b)/2
TRAPEZIO = TRAPEZIO_1 * c
QUADRADO = b**2
RETANGULO = a * b
print("TRIANGULO: {0:.3f}" .format(TRIANGULO))
print("CIRCULO: {0:.3f}" .format(CIRCULO))
print("TRAPEZIO: {0:.3f}" .format(TRAPEZIO))
print("QUADRADO: {0:.3f}" .format(QUADRADO))
print("RETANGULO: {0:.3f}" .format(RETANGULO))
