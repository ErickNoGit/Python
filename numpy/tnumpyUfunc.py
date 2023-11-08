import numpy as np

print('NumPy fornece funções matemáticas familiares, como sin(), cos() e exp(). No NumPy, eles são chamados de "funções universais" (ufunc). No NumPy, essas funções operam elementwise em uma matriz, produzindo uma matriz como saída (ndarray).\n')

print('Criando arrays\n')
a = np.array([2, 4, 9, 16])
print('Este é o nosso array:')
print(a, '\n')
print('Características:')
print('ndim: {}, dtype: {}, shape: {}, type: {}\n'.format(a.ndim, a.dtype, a.shape, type(a)))
# Buscando o sin()
print('Obtendo o valor do seno com np.sin()')
print(np.sin(a), '\n')

# Buscado o cos()
print('Obtendo o valor do cosseno com np.cos()')
print(np.cos(a), '\n')

# Buscando o exp()
print('Obtendo o valor do exponencial com np.exp()')
print(np.exp(a), '\n')

# Buscando a sqrt()
print('Obtendo o valor da raiz com np.sqrt()')
print(np.sqrt(a), '\n')

a = np.sqrt(a[0])
a = a**2
print(a, '\n')

# Indexação, Fatiamento e Iteração
print('Unidimensional as matrizes podem ser indexadas, fatiadas e iteradas, muito parecido listas e outras sequências de Python.\n')

print('Indexadas')
m = np.arange(2, 5)**3
print(m, '\n') # [ 8 27 64]

print('Fatiamentos')
print(m[0:1], '\n') # [8]

print('Iteracao')
print(m[0:2:2] + 5, '\n') # 13

# Multidimensao
def f(x, y):
	return 10 * x + y

print('fromfunction')
m = np.fromfunction(f, (2, 3), dtype=np.int64)
print(m, '\n')

print('Equivalencia')
print('A expressão entre colchetes em b[i] é tratado como um i seguido por tantas instâncias de : conforme necessário para representar o eixos restantes. O NumPy também permite que você escreva isso usando pontos como .b[i, ...]\n')

print('O pontos (...) representam quantos dois dois pontos necessários para produzir um tupla de indexação completa. Por exemplo, se x é uma matriz com 5 eixos, então\n')

# x[1, 2, ...] e equivalente a, x[1, 2, :, :, :]

c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c.shape) # (2, 2, 3)
print(c[1, ...])  # same as c[1, :, :] or c[1]
# array([[100, 101, 102],
#        [110, 112, 113]])
print(c[..., 2], '\n')  # same as c[:, :, 2]

print('Se quiser usar um operador em cada elemento da matrix, se usa flat')

for e in c.flat:
	print(e)




