saldo = 1500
valor_saque = 0

def sacar(valor):
    global saldo  
    global valor_saque
    if valor <= saldo:
        saldo = saldo - valor
        valor_saque = valor
        print(f"Você sacou R$ {valor:.2f}")
    else:
        print("Saldo insuficiente!")

def depositar(valor):
    global saldo 
    saldo = saldo + valor
    print(f"Você depositou R$ {valor:.2f}")

def extrato():
    print(f"Saldo em conta: R$ {saldo:.2f}")


print("[1 Sacar] [2 Depositar] [3 Saldo] [4 Sair]")

opcao = 1

while opcao != 4:
    opcao = int(input("\nDigite um número: "))
    if opcao == 1:
        valor = int(input("\nQuando voce quer sacar?"))
        if valor_saque < 500:
            sacar(valor)
        else:
            print("Valor de saque diário atingido")
    elif opcao == 2:
        valor = int(input("\nQuando voce quer depositar?"))
        depositar(valor)
    elif opcao == 3:
        extrato()

print("VOCE SAIU DO PROGRAMA")