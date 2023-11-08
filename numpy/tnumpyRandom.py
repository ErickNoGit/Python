import numpy as np
import pandas as pd

# Random teste
a = np.array([3, 2], dtype=np.int64)
print(a)

a += 200
print(a)

s = pd.Series(np.array([2, 3, 5, 6, 7, 10]))
print(s)

s += 2
print(s)

# Construindo DataFrame
df = pd.DataFrame(np.arange(1, 55).reshape(6, 9))

print(df)

# Progressao aritmetica com linspace(1, 1, 1)
l = np.linspace(1, 9, 2)
#progrssao inutil, o objetivo e fazer varios flutuantes
print(l)

l = np.linspace(1, 9, 10)
#funcionou
print(l)

# transformando em inteiro
l = np.array(list(l), dtype=np.int64)
print(l)

# retorno => [1 1 2 3 4 5 6 7 8 9]
# Objetivo : pegar o 1, somar com 9, pegar 10
# colocar depois do 9 e eliminar o 1
l = list(l)
um = l.pop(0)
nove = l[8]
soma = nove + um
l.append(soma)
print(np.array(l))
















