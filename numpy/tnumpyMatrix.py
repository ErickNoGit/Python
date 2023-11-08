import numpy as np

# Matrizes e suas impressoes no print
# Matriz 1D
print('Essa e uma matrix 1-dimensao')
d1 = np.arange(10, 15, 1)
print('ndim: {}, dtype: {}, shape: {}, type: {}'.format(d1.ndim, d1.dtype, d1.shape, type(d1)))
print(d1, '\n')

# Matriz 2D
print('Essa e uma matrix 2-dimenssoes')
d2 = np.arange(10, 16, 1).reshape(3, 2)
print('ndim: {}, dtype: {}, shape: {}, type: {}'.format(d2.ndim, d2.dtype, d2.shape, type(d2)))
print(d2, '\n')

# Matriz 3D
print('Essa e uma matrix 3-dimenssoes')
d3 = np.arange(10, 22, 1).reshape(2, 3, 2) # Z, X, Y
print('ndim: {}, dtype: {}, shape: {}, type: {}'.format(d3.ndim, d3.dtype, d3.shape, type(d3)))
print(d3, '\n')

# Fixacao
print('Matrizes numpy possuem diverssas dimenssoes (ndim)')
print('Cada dimenssao e um conjunto de lista se n >= 2')
print('Ela sempre retorna um objeto numpy.ndarray \n')

# tentando alterar tipos de dados
print('Vamos alterar a primeira posicao d1[0] = "a"')
try:
	d1[0] = 'a'
except:
	print('Nao funciona, deu erro \n')

print('Vamos alterar tudo entao: em d1[:] = "a"')
try:
	d1[:] = 'a'
except:
	print('Nao funciona, deu erro novamente \n')

# Numpy nao aceita troca de valores em tipos de dados
print('d1 continua sendo d1 original')
print(d1, '\n')

# Grandes valores sao impressos no comeco e fim, o meio e oculto
print('Valores muito grandes sao ocultados no centro')
ga = np.arange(10000)
print(ga, '\n')

# Para ver toda a matrix pode-se usar np.set_printoptions(threshold=sys.maxsize)
print('np.set_printoptions(threshold=sys.maxsize)\n')

# Operacoes basicas com matrizes
print('Operadores aritméticos nas matrizes se aplicam elementwise. Uma nova matriz é criado e preenchido com o resultado.')

a = np.array((1, 2, 3))
b = np.array([4, 5, 6])
c = b - a
print('a = [1, 2, 3] e b = [4, 5, 6], ele subtrai pelo mesmo index')
print('c = b - a')
print(c, '\n')

# Se ele faz por index, e uma economia do que fariamos por cada um
print('Aqui, na operacao python, c, volta a ser uma lista python')
c = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
print(c, '\n')
print('Ele nao e um ndarray')
try:
	c.ndim
except:
	print('Usou-se c.ndim e deu erro')

# para operadores de inteiros e flutuantes em += e *= nao funciona
print('Numpy consegue entender que inteiros viram flutuantes')
a = np.arange(10).reshape(5, 2)
b = np.array([[1, 1],
			  [1, 1],
			  [1, 1],
			  [1, 1],
			  [1, 1]], dtype=np.float64)
print(a, '\n')
print(b, '\n')

# operando b += a (sobrescreve a), que e inteiro, o inverso da erro
b += a
print(b, '\n')

# Multiplicando a *= 3.2 da falso, da erro, mas se for int da true
try:
	a *= 3.2
except:
	print('a*=3.2, Nao pode multiplicar flutuante por operador *= contendo inteiros, deu erro:\n')

# Mas assim funciona (int por int)
print('a *= 3 da true, todos os valores dos index sao multiplicados por 3')
a *= 3
print('A multiplicacao com o inteiro 3: \n {}'.format(a))

# Do contrario, flutuante para flutuante, funciona
print('\n')
print('b *=3.2, da true valores de b sao multiplicados por 3.2')
b *= 3.2
print(b, '\n')

# Matrizes flutuantes funcionam com inteiros mas nao o contrario
print('Com inteiros de b *= 10')
b *= 10
print(b, '\n')

# Numpy aceita operacao aritmetica com sum(), min(), max()
print('Esse é o array numpy "a"')
print(a, '\n')
print('Para .sum(), aceita-se axis=0 para colunas, e axis=1 para linhas')
soma = a.sum(axis=0)
print('a.sum(axis=0) \n', soma)
print('\n')
soma = a.sum(axis=1)
print('a.sum(axis=1) \n', soma)
print('Independente de ele somar por linha ou coluna')
print('Ele retorna um array de 1 dimensaao derivado a quantidade de coluna e linhas')
print('se a tem 2 colunas, ele retorna um ndarray de 1 dimensao com dois valores, a soma de ambas as colunas, da esquerda para direita')
print('quando se trata de linhas, ele soma de cima para baixo, linha a linha da esquerda para direita, retonando um ndarray de uma dimensao!\n')
#---------
# 13-06-2023
# min e max
print('Essa é o array numpy de "A"')
print(a, '\n')

print('Esse é o valor minimo de a.min()')
print(a.min(), '\n')
# Ele leu todo array e retornou o menor valor
print('Utilizando axis=0(colunas) e axis=1(linhas)\n')
print('axis=0 (colunas)')
print(a.min(axis=0), '\n')
# Ele esta lendo coluna por coluna e retornando ndarray de 1 dimensao
# com todos os menores valores por coluna
print('axis=1 (linhas)')
print(a.min(axis=1), '\n')
# Ele le cada array por linha, retorna 1 array de 1 dimensao com
# o menor valor de cada linha
print('A função .mean(), porém, é a média da soma de todos os valores')
print('A média de a é:')
print(a.mean(), '\n')
# Ele leu todo array, somou tudo, e dividiu pela quantidade de valores
# Retornou um número
# Usando axis
print('Mostrando axis=0 (colunas)')
print(a.mean(axis=0), '\n')
# Ele leu coluna por coluna, somou, e dividiu pelo tamanho da mesma
# Ele retorna um ndarray de 1 dimensao com a media de cada coluna
print('Mostrando axis=1 (linhas)')
print(a.mean(axis=1), '\n')
# Ele leu linha por linha e tirou a media de cada uma pelo tamanho
# da linha

print('Criando arrays com retornos de min(), mean(), max()\n')
print('Esse é o valor minimo que não sofre dtype')
c = np.array([[13, 12, 13, 14, 15], [14, 14, 12, 15, 13]])
retorno = c.min()
print('Type: {}, ndim: {}, dtype: {}'.format(type(retorno), retorno.ndim, retorno.dtype))
print(retorno, '\n')

print('Esse é o valor médio alterado para inteiro')
c = np.array([[13, 12, 13, 14, 15], [14, 14, 12, 15, 13]])
retorno = c.mean(dtype=np.int64)
print('type: {}, ndim: {}, dtype: {}'.format(type(retorno), retorno.ndim, retorno.dtype))
print(retorno, '\n')

print('Esse é o valor máximo que não sofre dtype')
c = np.array([[13, 12, 13, 14, 15], [14, 14, 12, 15, 13]])
retorno = c.max()
print('Type: {}, ndim: {}, dtype: {}'.format(type(retorno), retorno.ndim, retorno.dtype))
print(retorno, '\n')

#Trabalhando com .sum()
print('.sum() seguindo os parametros de dtype e axis')
s = np.array([[13, 12, 13, 14, 15], [14, 14, 12, 15, 13]])
print(s, '\n')
print('Somando por colunas (axis=0)')
soma = s.sum(axis=0, dtype=np.float64)
print(soma, '\n')
# O index 0 da 0 lista do ndarray, é 13, o index 0 da 1 lista do
# ndarray é 14, portanto 13 + 14 = 27, ele retorna inteiro e foi
# transformado e flutuante, ele fez isso para cada index em cada lista
print('Somando por linhas (axis=1)')
s = np.array([[13, 12, 13, 14, 15], [14, 14, 12, 15, 13]])
soma = s.sum(axis=1, dtype=np.float16)
print(soma, '\n')

# Tentando concatenar string em arrays
print('Mostrando o array inteiro')
array = np.array([1, 2, 3, 4, 5], dtype=np.int64)
print(array, '\n')
print('Transformando em string')
array = array.astype(str)
print(array, '\n')

#lista = list(array)
resultado = ';'.join(array)
print(resultado)
print(type(resultado))







