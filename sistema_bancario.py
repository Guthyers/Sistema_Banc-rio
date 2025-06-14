
menu = """
======== MENU ========
    [D] DEPOSITAR
    [S] SACAR
    [E] EXTRATO
    [Q] SAIR
======================
"DIGITE A OPÇÃO DESEJADA:"""

saldo  = 0
limite = 500
extrato = ""
numero_de_saque = 3
limite_saque = 0


while True:
    opcao = input(menu).upper()
    

    if opcao == "D":
        valor = float(input("Digite o valor do seu deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
        else:
            print("Valor de deposito inválido!")

    elif opcao == "S":
        valor = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_de_saque >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! saldo insuficiente")
        elif excedeu_limite:
            print("Operação indisponível! O valor do saque excedeu o limite")
        elif excedeu_saque:
            print("Operção falhou! Números de saque excedidos")

        elif valor > 0:
            saldo -= valor
            extrato = f'Saque: R$ {valor:.2f}\n'
            numero_de_saque += 1

        else:
            print("Operação falhou! valor informado é invalido")

    elif opcao == "E":
        print ("\n======== EXTRATO ========")
        print("Não foram ralizadas movimentações" if not extrato else extrato)
        print(f"\n Saldo: {saldo:.2f}")
        print("=========================")
        
    elif opcao == "Q":
        print("você saiu da operação")
        break

    else:
        print("operação Inválida...")