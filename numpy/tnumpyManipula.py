import numpy as np

# Manipulação de forma
print('Alterando a forma de uma matriz')
a = np.ones([3, 4], dtype=np.int64)
print('dtype: {}, ndim: {}, shape: {}, type: {}'.format(a.dtype, a.ndim, a.shape, type(a)))
print(a, '\n')

b = a.copy()
# A forma de uma matrix pode ser alterada com n-comandos
print('3 tipos principais: .ravel(), .reshape(), .T')
# O ravel() retorna um array de uma dimenssão [1, 2, 3]
print('Array com .ravel()')
b = b.ravel()
print(b)
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(b.dtype, b.ndim, b.shape, type(b)))

# O reshape() retorna um array com dimenssões no argumentos
print('Array com .reshape()')
b = a.copy()
b = b.reshape(2, 6)
print(b)
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(b.dtype, b.ndim, b.shape, type(b)))

# .T retorna o array transposed
print('Usando .T')
print('De forma prática, ele inverte o x pelo y')
b = b.T
print(b)
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(b.dtype, b.ndim, b.shape, type(b)))

# aplicando conversões
print('Vamos converter tipos de dados nos arrays com np.astype()')
matriz = np.array([1, 2, 3.2])
print('matriz = np.array([1, 2, 3.2]) \n')
print(matriz)
print('Conferindo tipos de dados')
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(matriz.dtype, matriz.ndim, matriz.shape, type(b)))

# vamos tentar alterar de float para inteiro
print('Alteração com np.astype() : {} agora eles são int64'.format(matriz.astype(int)))

# vamos converter para string agora
print('Alteração com np.astype() : {} agora eles são string'.format(matriz.astype(str)))

# Vamos buscar seus dados basicos
b = matriz.astype(str)
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(b.dtype, b.ndim, b.shape, type(b)))

# Vamos devolver para float
print('Alteração com np.astype() : {} agora eles são float'.format(matriz.astype(float)))

b = matriz.astype(float)
print('dtype: {}, ndim: {}, shape: {}, type: {} \n'.format(b.dtype, b.ndim, b.shape, type(b)))


