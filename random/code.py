# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = [0, 1, 2, 3, 4]
print(vetor[:])

# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vetor[::-1])

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = [9, 3, 6, 8]
print(notas)
# soma = notas[0]+notas[1]+notas[2]+notas[3]
media = (notas[0]+notas[1]+notas[2]+notas[3]) / 4
print(media)

# Faça um Programa que leia um vetor de 10 itens, e diga quantas letras foram lidas. Imprima as letras.
vetor1 = ['a', 'b', 3, 5, 'c', 'd', 3, 'e', 'f', 2]
tipoConsoante = type(vetor1[0])
listaLetras = []

for i in vetor1[0::1]:
    if (str == type(i)):
        if (not i.isnumeric()):
            listaLetras.append(i)

print('essa é a quantidade de letras:', len(listaLetras))
print(listaLetras, '\n')

# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetor2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
listaConsoante = []
'''
vetor2.remove('a')
vetor2.remove('e')
vetor2.remove('i')

print('há esse número de consoantes:',len(vetor2))
print(vetor2)

'''
for i in vetor2[::1]:
  if (i == 'a'):
    vetor2.remove('a')
    #listaConsoante.append(vetor2)
  elif(i == 'e'):
    vetor2.remove('e')
    #listaConsoante.append(vetor2)
  elif(i == 'i'):
    vetor2.remove('i')
    listaConsoante.append(vetor2)

print('O número de consoantes é : ',len(listaConsoante[0][:]),'\n', listaConsoante,'\n')

'''
  elif (i != 'e'):
    listaConsoante.append(i)
  elif (i != 'i'):
    listaConsoante.append(i)  
  elif (i != 'o'):
    listaConsoante.append(i) 
  elif (i != 'u'):
    listaConsoante.append(i)
'''

#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
vetorAdd = []

for i in range(21):
  vetorAdd.append(i)

vetorPar = [vetorAdd[2::2]]
vetorImpar = [vetorAdd[1::2]]

print('impares:',vetorImpar)
print('pares:',vetorPar)
vetorAdd.remove(0)
print('Com todos Inteiros:',vetorAdd,'\n')

#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

i = 1
aluno = []

while (i <= 10):
  print('Aluno', i,'\n')
  nota1 = float(input('Digite sua primeira nota: '))
  nota2 = float(input('Digite sua segunda nota: '))
  nota3 = float(input('Digite sua terceira nota: '))
  nota4 = float(input('Digite sua quarta nota: '))
  print('='*10, '\n')

  media = (nota1 + nota2 + nota3 + nota4) / 4
  if (media > 7.0):
    aluno.append(media)
  i += 1

print('Dos 10 alunos %d passaram!' %(len(aluno)))


#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor4 = [1, 2, 3, 4, 5]

soma = vetor4[0] + vetor4[1] + vetor4[2] + vetor4[3] + vetor4[4]

multiplica = vetor4[0] * vetor4[1] * vetor4[2] * vetor4[3] * vetor4[4]
 
print('soma:', soma)
print('multiplicação:', multiplica)