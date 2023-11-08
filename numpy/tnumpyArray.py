import numpy as np
import math

# Criando matrix n-dimensional
m = np.arange(1, 51).reshape(5, 10)
print(m, '\n')

# acessando e trocando
m[1][0:len(m[0]):2] = (m[0][3] + 76) - 2 * (4 * 10)

print(m, '\n')

# criando um array com objeto numpy.array()
a = np.array([[1, 2, 3, 4], 
			  [2, 4, 6, 8]], dtype=np.float64)

print('ndim: {}, dtype: {}'.format(a.ndim, a.dtype))
print(a, '\n')

tri_d = np.array([[[1, 2, 3],
				   [4, 5, 6],
				   [7, 8, 9]],
		
				  [[1, 1, 1],
				   [1, 1, 1],
				   [6, 7, 8]]], dtype=np.int64)

print('ndim: {}, dtype: {}'.format(tri_d.ndim, tri_d.dtype))
print(tri_d, '\n')

z = np.zeros([4, 4], dtype=np.int64)

print('ndim: {}, dtype: {}'.format(z.ndim, z.dtype))
print(z, '\n')
# valores  : z, x, y
o = np.ones((3, 4, 4), dtype=np.float64)

print('ndim: {}, dtype: {}'.format(o.ndim, o.dtype))
print(o, '\n')

o[0][0] = 2
print('Alterei os ones e retornei os twos')
print(o[0], '\n')

e = np.empty([3, 3])

print('ndim: {}, dtype: {}'.format(e.ndim, e.dtype))
print(e, '\n')

# iteracao em array numpy
# no python existe essa funcao:
my_list = list(range(1, 10))
# armazena em 'my_list' uma lista de sequencia de 1 a 9
print(my_list, '\n')
# segue 3-S. START, STOP, STEP (inicio, parada, sequencia)
# No numpy devolve um ndarray
my_array = np.arange(1, 10)
print('ndim: {}, dtype: {}, type: {}'.format(my_array.ndim, my_array.dtype, type(my_array)))
print(my_array, '\n')

# Podemos transformar em lista python novamente
my_list = list(my_array)
print(my_list, '\n')

# Podemos iterar sobre os objetos
for i in my_array[::]:
	print(i)

print('------------------------')

for i in my_list[::]:
	print(i)

# Limitando em float em sequencia (arimetc progression)
f = np.arange(0, 2, 0.25)
print(f, '\n')

# transformando em lista
g = f
print(list(g), '\n')

# comparando
if (g[0] == f[0]):
	print('True!!')
else:
	print('False!')

# Para criacao de flutuante, devido a imprecisao usase lispace
# recebe valor, inicial, ate final, em n-sequencia = int64
l = np.linspace(-1, 1, 5)
print('Crie n-sequencia de escala -1 ate 1')
print('ndim: {}, dtype: {}, type: {}'.format(l.ndim, l.dtype, type(l)))
print(l, '\n')

# Criando uma matrix 2D com linspace para plano cartesiano
# 0 = vazio, exceto ponto interseccao
print('Usando objeto, dentro de array')
cart = np.array([[0, 0, 1.0, 0, 0], 
				[0, 0, 0.5, 0, 0],
				np.linspace(-1, 1, 5),
				[0, 0, -0.5, 0, 0],
				[0, 0, -1.0, 0, 0]])

print('ndim: {}, dtype: {}, type: {}'.format(cart.ndim, cart.dtype, type(cart)))
print(cart, '\n')

# Calculo do triangulo retangulo do plano cartesiano (PC)
print('Se do ponto 0 ate altura 1, e distancia 0.5, qual hipotesuna?')
h = (cart[0][2] ** 2) + (cart[2][3] ** 2)
res = math.sqrt(h)
print('A hipotenusa e: {:.2f} \n'.format(res))

# numeros pequenos criam floats base .0
lin = np.linspace(5, 9, 3)
print('ndim: {}, dtype: {}, type: {}'.format(lin.ndim, lin.dtype, type(lin)))
print('Usando n-sequencia menor que x inicial e y final =>')
print(lin, '\n')

# Numeros grandes criam floats de progressao
lin = np.linspace(5, 9, 10)
print('ndim: {}, dtype: {}, type: {}'.format(lin.ndim, lin.dtype, type(lin)))
print('Usando n-sequencia maior que x incial e y final =>')
print(lin, '\n')
