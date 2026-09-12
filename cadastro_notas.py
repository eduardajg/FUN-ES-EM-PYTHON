# Solicita o nome do aluno
Aluno = input('Digite o nome do Aluno: ')

# Cria uma lista vazia para armazenar as notas
Nota = []

# Solicita as notas e converte o valor digitado para número decimal
Nota_1 = float(input('Digite a primeira nota: '))
Nota_2 = float(input('Digite a segunda nota: '))
Nota_3 = float(input('Digite a terceira nota: '))

# Adiciona as notas à lista
Nota.append(Nota_1)
Nota.append(Nota_2)
Nota.append(Nota_3)

# Calcula a média das três notas
Media = (Nota_1 + Nota_2 + Nota_3) / 3

# Verifica se a média é maior ou igual a 7
if Media >= 7:
 Situaçao = 'Aprovado'
# Caso a média seja menor que 7
else:
 Situaçao = 'Reprovado'

print(f'======= Relatório final =======')
print(f'Aluno: {Aluno}')
print(f'Notas: {Nota}')
print(f'Média: {Media}')
print(f'Situação do aluno: {Situaçao}')