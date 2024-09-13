# declarando listas em python

# listas como array
frutas = ["laranja", "maca", "uva"]
print(frutas)

# lista vazia
frutas = []
print(frutas)

# lista como objeto iterador - recebe um parametro iteração
letras = list("python") 
print(letras) # saida ['p', 'y', 't', 'h', 'o', 'n']

# outro exemplo de lista de iteração
numeros = list(range(10))
print(numeros) # saida [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# lista com objetos diferentes 
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# manipulando a lista com indice
print(carro[0])
print(carro[1])
print(carro[-1]) # ultimo item da lista

#iterando listas
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)