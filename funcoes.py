def salvar_carro(nome, marca, ano):
        print(f"Salvando o carro -> {nome}/{marca}/{ano}")


salvar_carro("Uno", "Fiat", 1999)

def soma(*numeros):
    return sum(numeros)

print(soma(5,5,2)) 

def informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

informacoes(nome="Carolina", idade=19, curso="ADS", cidade="Taquari")