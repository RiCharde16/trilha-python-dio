menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

DEPOSITO_TXT = """ 
--------------------------------------------
    Deposito realizado na conta no valor de:
        R$ {:.2f}
--------------------------------------------
"""

SAQUE_TXT =  """ 
-------------------------------------------
    Saque realizado na conta no valor de:
        R$ {:.2f}
-------------------------------------------
"""
SALDO_ATUAL_CONTA_TXT = """ 
------------------------------------------
    Saldo atual da conta: R$ {:.2f}
------------------------------------------
"""


while True:

    opcao = input(menu)

    print()

    if opcao == "1":
        print("Depósito".center(80,"-"))

        valor_deposito = float(input("Digite um valor para depositar: "))
        print()

        if(valor_deposito <= 0):
            print("Valor do Deposito invalido".center(50))

        else:
            saldo += valor_deposito

            print(f"Depósitado R$ {valor_deposito:.2f} na conta")
            extrato += DEPOSITO_TXT.format(valor_deposito)
    
    elif opcao == "2":
        print("Saque".center(80,"-"))

        print(f"Você possui {LIMITE_SAQUES - (numero_saques)} saques diarios".center(80))

        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input(f"Digite um valor para sacar dentro do limite de R$ {limite}: "))
            print()

            if valor_saque > limite:
                print(f"escolha um valor de saque dentro do limite de R$ {limite} !".center(80))
            
            elif valor_saque > saldo:
                print("valor do saque maior que o saldo da sua conta".center(80))
            
            elif valor_saque <= 0:
                print("Valor de saque invalido".center(50))
            else:
                saldo -= valor_saque
                numero_saques += 1

                print(f"Sacado R$ {valor_saque:.2f} na conta")
                extrato += SAQUE_TXT.format(valor_saque)

        else:
            print("Não e possivel realizar mais saques hoje volte amanha".center(80))

    elif opcao == "3":
        print("Extrato".center(80,"-"),end=" ")

        print("\n\nNão foram realizadas movimentações na conta".center(80) if not extrato else extrato)
        print(SALDO_ATUAL_CONTA_TXT.format(saldo))
    
    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.".center(80))

print("Programa Finalizado\n".center(80))