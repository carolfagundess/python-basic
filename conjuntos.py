# Estrutura de dados SET
# Colecao de objetos unicos, sem repeticoes
# Usado para eliminar itens duplicados de um iteravel


numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

numeros = list(numeros)
print(numeros[0])

for numero in numeros:
    print(numero)

# funcao enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")