import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_de_saque >= limite_saque

    if excedeu_saldo:
        print("\n@@@ Operação falhou, você não tem saldo suficiente @@@")

    elif excedeu_limite:
        print("\n@@@ valor do saque excede limite @@@")

    elif excedeu_saque:
        print("\n@@@ Limite de saque excedido @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR${valor:.2f}\n'
        numero_de_saque += 1
        print("\n=== Saque realizado com sucesso! ===")
    return  saldo, extrato

def exibir_extrato( saldo, /, *,  extrato):
    print("===== EXTRATO =====")
    print("Não houve movimentação." if not extrato else extrato)
    print(f'\nSeu saldo é de: R$ {saldo:.2f}')
    print("===================")

def criar_usuario(usuarios):
    cpf = input("digite seu CPF (somente números): ")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse cpf @@@")
        return
    
    nome = input("informe seu nome completo:")
    data_de_nascimento = input("informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe seu endereço (logradouro - nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Digite CPF do usuário(apenas números): ")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario:
        print("\n=== Usuário criado com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("@@@ Usuário não encontrado @@@")

def listar_contas (contas):
    for conta in contas:
        linha = f"""\
             Agência:\t{conta['agencia']}
             C/C:\t\t {conta['numero_conta']} 
             Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main(): 
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    saldo  = 0
    limite = 500
    extrato = ""
    numero_de_saque = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()
        

        if opcao == "d":
            valor = float(input("Digite o valor do seu deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_de_saque = numero_de_saque,
                limite_saque = LIMITE_SAQUE,
            )

        elif opcao == "e":
            exibir_extrato (saldo, extrato=extrato)
        
        elif opcao =="nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len (contas) + 1
            conta = criar_conta (AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
    
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break

        else:
            print("operação Inválida...")

main ()