valor_saldo = 2500
depositado = []
sacado = []

def consultar_saldo():
    print(valor_saldo)

def depositar():
    global valor_saldo

    deposito = float(input("qual valor que depositar? "))
    if deposito > 0:
        valor_saldo = valor_saldo + deposito
        depositado.append(deposito)
    else:
        print("Digite um valor valido")

def sacar():
    global valor_saldo

    sacar = float(input("Qual valor deseja saca? "))

    if sacar <= valor_saldo:
        valor_saldo = valor_saldo - sacar
        print("Valor retirado")
        sacado.append(sacar)
    else:
        print("Valor de saque maior que o de salt, por fanor saque um valor menor")

def extrato():
    print("\n========== EXTRATO ==========")
    print(f"Valor depositado {depositado}")
    print(f"Valor sacado {sacado}")
    print(f"Saldo atual: R$ {valor_saldo:.2f}")
    print("==============================")

def menu():
    while True:
        print("\n==============================")
        print("        Caixa eletronico")
        print("==============================")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Extrato")
        print("5 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_saldo()

        elif opcao == "2":
            depositar()

        elif opcao == "3":
            sacar()

        elif opcao == "4":
            extrato()

        elif opcao == "5":
            print("\nSaindo do caixa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

menu()