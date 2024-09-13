# Classe dict
# Um conjunto não ordenado de pares (chave e valor)
# valores de chaves unicos e objetos mutaveis

pessoa = {"nome": "Carol", "idade": 19}
print(pessoa)

# mesma declaracao com construtor dict
pessoa = dict(nome="Carol", idade=19)
print(pessoa)

# adicionando uma nova chave com valor
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

# como acessar os dados
print(pessoa["nome"])

# alterando
pessoa["idade"] = 20
print(pessoa["idade"])

# Dicts alinhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# acessando um dado
print(contatos["chappie@gmail.com"]["nome"])