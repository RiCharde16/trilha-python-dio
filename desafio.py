def saque(*,saldo,valor,extrato,limite=500, numero_saques, limite_saques=3):
    if valor > saldo:
        print(f"Valor de saque R$ {valor} excede o saldo da conta R$ {saldo}") 
    elif valor > limite:
        print(f"valor excedo o limite de {limite}")
    else:
        saldo -= valor
        print(f"Saque de {valor:.2f}")
        numero_saques += 1
        extrato = f""" 
-------------------------------------------
    Saque realizado na conta no valor de:
        R$ {valor:.2f}
-------------------------------------------
"""
        return saldo, extrato, numero_saques
    
    return saldo, "", numero_saques

def deposito(saldo,valor,/):
    extrato = f""" 
--------------------------------------------
    Deposito realizado na conta no valor de:
        R$ {valor:.2f}
--------------------------------------------
"""
    saldo += valor 
    return saldo, extrato

def extrato(saldo,/,*,extrato):
    print("Extrato".center(80,"-"),end=" ")

    print("\n\nNão foram realizadas movimentações na conta".center(80) if not extrato else extrato)
    print(""" 
------------------------------------------
    Saldo atual da conta: R$ {:.2f}
------------------------------------------
""".format(saldo))

def cadastrar_usuario(lista_usuarios):
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite a sua data de nascimento EX: XX/XX/XXXX: ")
    lista_data = data_nascimento.split("/")
    if len(lista_data) == 3:
        verificar_dia = (len(lista_data[0]) > 2 and not lista_data[0].isnumeric())
        verificar_mes = (len(lista_data[1]) > 2 and not lista_data[1].isnumeric())
        verificar_ano = (len(lista_data[2]) > 4 and not lista_data[2].isnumeric())
        if verificar_dia and verificar_mes and verificar_ano:
            print("os valores da Data estão incorreto")
            return 
    else:    
        print("Data de nascimento invalida")
        return 

    cpf = input("Digite seu cpf apenas numeros: ")

    if not cpf.isnumeric() or (len(cpf) > 11 or len(cpf) < 11):
        print("CPF Invalido".center(80))
        return
    
    for usuario in usuarios_cadastrados:
        if (usuario['cpf'] == cpf):
            print("Usuario Já Cadastrado com esse CPF".center(80))
            return 
        
    endereco = input("Digite seu endereco ex: \nlogadouro - numero - bairro - cidade - estado \n => ")
    
    endereco_lista = endereco.split("-")
    cond1 = len(endereco_lista ) < 5 or len(endereco_lista) > 5
    cond2 =  not endereco_lista[1].strip().isdigit()

    if(cond1 or cond2):
        print("Endereco invalido".center(80))
    else: 
        endereco = f"{endereco_lista[0].strip()}, {endereco_lista[1].strip()} - {endereco_lista[2].strip()} - {endereco_lista[3].strip()} - {endereco_lista[4].strip()}"
        usuario = {"cpf":cpf,"nome": nome.title(), "data de nascimento": data_nascimento, "endereco": endereco.lower()}

        print("usuario cadastrado com sucesso !".center(80))
        lista_usuarios.append(usuario)
    
    return

def cadastrar_conta(lista_conta,usuario, numero_conta):
    nova_conta = {"agencia": "0001", "numero da conta": numero_conta, "usuario": usuario, "saldo": 0, 'extrato': "",'numero saques': 0}

    lista_conta.append(nova_conta)
    print(f"Conta Criada para o usuario {usuario['nome']} com o CPF: {usuario['cpf']}")

def menu_inicial():
    menu = """
 [1] Cadastrar usuario
 [2] acessar sua conta de usuario
 [0] sair

=> """ 
    opcao = input(menu)

    if opcao == "1":
        cadastrar_usuario(usuarios_cadastrados)
        menu_inicial()

    elif opcao == "2":
        if usuarios_cadastrados:
            print("INDEX\t| NOME USUARIO")
            for index, usuario in enumerate(usuarios_cadastrados):
                print(f"{index}\t| {usuario['nome']}")

            print()
            cpf_user = input("acesse seu usuario pelo seu CPF: ")
            
            if(cpf_user.isnumeric()):
                for usuario in usuarios_cadastrados:
                    if(cpf_user == usuario['cpf']):
                        print("usuario encontrado !".center(80))
                        menu_usuario(usuario)
                        break
                else:
                    print("Usuario não econtrado".center(80))
            else:
                print("Usuario invalido !".center(80))

        else:
            print("Não a usuarios cadastrados".center(80))
            menu_inicial()

    elif opcao == "0":
        return False
    
    else:
        print("Opcao invalida".center(80))
    
    return True

def menu_usuario(usuario):

    menu_user = f"""
Bem-Vindo {usuario['nome']}

 [1] Cadastrar conta bancaria
 [2] listar as contas bancarias do usuario
 [3] acessar conta bancaria
 [4] verificar seus dados
 [5] voltar ao menu inicial

=> """

    opcao_user = input(menu_user)

    if opcao_user == "1":
        if not contas_cadastradas:
            numero = 1
        else:
            numero = len(contas_cadastradas)+1
        
        cadastrar_conta(contas_cadastradas,usuario,numero)
        menu_usuario(usuario)
    
    elif opcao_user == "2":
        print(f"Contas Cadastradas no usuario {usuario['nome']}".center(80))
        
        if(contas['usuario'] == usuario  for contas in contas_cadastradas):
            for index,conta in enumerate(contas_cadastradas):
                if conta['usuario']['cpf'] == usuario['cpf']:
                    print(index, f"'numero da conta': {conta['numero da conta']} 'agencia': {conta['agencia']} 'saldo': {conta['saldo']}" )
        else:
            print("usuarios sem contas bancarias".center(80))
        
        menu_usuario(usuario)
    
    elif opcao_user == "3":
        if contas_cadastradas:
            print()
            op_conta = input("Digite o numero da sua conta: ")
            for conta in contas_cadastradas:
                if (int(op_conta) == conta['numero da conta'] and conta['usuario']['cpf'] == usuario['cpf']):
                    print(f"Conta com o numero {conta['numero da conta']} acessada".center(80))
                    menu_conta(op_conta)
                    break
            else:
                print("Conta não encontrada".center(80))
        else:
            print(f"usuario {usuario['nome']} não possui contas cadastras".center(80))
        
        menu_usuario(usuario)
                
    elif opcao_user == "4":
        print("Dados do usuario".center(80,"-"))
        for chave,valor in usuario.items():
            print(f"{chave}: {valor}")
        menu_usuario(usuario)
    
    elif opcao_user == "5":
        return
    else:
        print("Opção invalida ".center(80))
        menu_usuario(usuario)

def menu_conta(numero_da_conta):
    menu_conta_bancaria = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] voltar ao menu do usuario

=> """
    for conta in contas_cadastradas:
        if (conta['numero da conta'] == int(numero_da_conta)):
            conta_usada = conta
            break

    opcao_conta = input(menu_conta_bancaria)

    if(opcao_conta == "1"):
        valor_deposito = input("Digite um valor para depositar: ")

        if valor_deposito.replace(".","",1).isdigit() and float(valor_deposito) > 0:
            valor_deposito = float(valor_deposito)
            saldo, extrato_deposito = deposito(conta_usada['saldo'],valor_deposito)

            conta_usada['extrato'] += extrato_deposito

            conta_usada['saldo'] = saldo

            print(f"Depositado: {float(valor_deposito):.2f}")
            menu_conta(numero_da_conta)
            
        else:
            print("Valor invalido".center(80))
            menu_conta(numero_da_conta)

    elif opcao_conta == "2":
        limite_saque_n = 3
        print(F"voce possui {limite_saque_n - conta_usada['numero saques']} saques disponiveis para hoje")

        valor_saque = input("Digite um valor para saque dentro do limite de R$ 500: ")
        if(conta_usada['numero saques'] < limite_saque_n):
            if valor_saque.replace(".","",1).isdigit() and float(valor_saque) > 0:
                saldo, extrato_saque, numero_saques = saque(saldo=conta_usada['saldo'],valor=float(valor_saque),extrato=conta_usada['extrato'],limite=500,numero_saques=conta_usada['numero saques'],limite_saques=3)
                conta_usada['saldo'] = saldo
                conta_usada['extrato'] += extrato_saque
                conta_usada['numero saques'] = numero_saques

                menu_conta(numero_da_conta)
        
            else:
                print("Valor invalido".center(80))
                menu_conta(numero_da_conta)
        else:
            print("sem saques disponiveis volte amanhâ".center(80))
    
    elif opcao_conta == "3": 
        extrato(conta_usada['saldo'],extrato=conta_usada['extrato'])
        menu_conta(numero_da_conta)
    
    elif opcao_conta == "4":
        return
    
    elif opcao_conta == "0":
        return
    
    else:
        print("opção invalida".center(80))
        menu_conta(numero_da_conta)
    
run = True
usuarios_cadastrados = []
contas_cadastradas = []
extratos = ""

while run:
    run = menu_inicial()

print("Programa Finalizado\n".center(80))