#Tipos de dados
# str -> texto
# int, float, complex -> numericos
# list, tuple, range -> sequencias
# dict -> map *chave - valor
# set, fronzet -> colecao
# bool -> booleano
# bytes, bytearray, memoryview -> bit binario

# nao existe constante, apenas variaveis
# comando snake case nome_variavel
#converter -> casting -> tipovariavel_nova(variavel_velha) -> 

preco = 10
print(float(preco))

# funcoes de entrada e saida builtin 
#input -> entrada padrao teclado - ler entrada
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
#print -> sep, end, file, flush 
print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")