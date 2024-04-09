from abc import ABC, abstractmethod
from datetime import datetime

# --------------- Classes Abstratas
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass 

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

# ---------------- Classes simples
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def menu_conta(self):
        menu_conta = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] voltar ao menu do usuario

=> """
        opcao_conta = input(menu_conta)

        print()
        if(opcao_conta == "1"):
            print(" Depositar ".center(80,"-"))
            valor_deposito = input("\nDigite um valor para depositar: ")
            if valor_deposito.replace(".","",1).isdigit():
                deposito = Deposito(float(valor_deposito))
                deposito.registrar(self)

                self.menu_conta()
            else:
                print("\n valor invalido".center(80))
                self.menu_conta()
        
        elif (opcao_conta == "2"):
            print(" Sacar ".center(80,"-"))
            valor_saque = input("\nDigite um valor para sacar dentro de R$ 500: ")
            if valor_saque.replace(".","",1).isdigit():
                saque = Saque(float(valor_saque))
                saque.registrar(self)

                self.menu_conta()
            else:
                print("\n Valor invalido".center(80))
                self.menu_conta(0)
            
        elif (opcao_conta == "3"):
            print(" Extrato ".center(80,"-"))
            if self.historico.transacoes:
                for indice, transacao in enumerate(self.historico.transacoes):
                    print(f"{indice}: {", ".join([f"{chave}={valor}" for chave,valor in transacao.items()])}")
                
                print(f"\nSaldo da conta: {self.saldo:.2f}")
            else:
                print("\nNenhuma transação foi efetuada nesta conta".center(80))
            
            self.menu_conta()

        elif (opcao_conta == "4"):
            return

        else:
            print("Opção Invalida".center(80))

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    # Propriedades da classe Conta
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    
    @saldo.setter
    def saldo(self, value):
        self._saldo += value
        # return self._saldo + value
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if (excedeu_saldo):
            print("\nsem saldo suficiente para sacar".center(80))

        elif valor > 0:
            self.saldo = -(valor)
            print("Saque realizado com sucesso!".center(80))

            return True
        
        else:
            print("\nOperação Falhou".center(80))

        return False


    def depositar(self, valor):
        if valor > 0:
            self.saldo = valor
            print("\nDeposito realizado com sucesso".center(80))
        
        else:
            print("\nOperação Falhou".center(80))
            return False
        
        return True

class ContaCorrente(Conta): 
    def __init__(self,numero, cliente, limite= 500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao['tipo'] == Saque.__name__]
            )
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques == self.limite_saques

        if excedeu_limite:
            print("\n operação falhou! valor de saque excede o limite".center(80))
        
        elif excedeu_saque:
            print("\n Operação falhou! Numero maximo de saques excedido")

        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            Numero da Conta:\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\t {self.saldo}
        """
    
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    # def __str__(self):
    #     return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)
    
    @staticmethod
    def filtrar_usuarios(cpf, usuarios):
        if usuarios:
            usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
            return usuarios_filtrados[0] if usuarios_filtrados else None
        else:
            return None
        
    @staticmethod
    def mostrar_usuarios(usuarios):
        for index, usuario in enumerate(usuarios):
            print(f"{index} Cliente: {usuario.nome} CPF: {usuario.cpf}") 
        
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    
    def menu_usuario(self, lista_contas):
        menu_user = f"""
Bem-Vindo {self.nome}

 [1] Cadastrar conta bancaria
 [2] listar as contas bancarias do usuario
 [3] acessar conta bancaria
 [4] verificar seus dados
 [5] voltar ao menu inicial

=> """

        opcao_user = input(menu_user)

        print()
        if opcao_user == "1":
            numero = len(lista_contas) + 1
            # print(numero, agencia, self)
            # print(self)
            conta = ContaCorrente.nova_conta(numero, self)
            self.adicionar_conta(conta)
            lista_contas.append(conta)

            print(f"conta criada para o titular {conta.cliente.nome}".center(80))

            self.menu_usuario(lista_contas)

        elif opcao_user == "2":
            if self.contas:
                print("Index \t|\t Conta".upper())
                for index,conta in enumerate(self.contas):
                    # print(f"{index} \t| Numero: {conta.numero} Agencia: {conta.agencia}")
                    print(f"{index} \t {conta}")
                
            else:
                print("Nenhuma conta neste usuario".center(80))

            self.menu_usuario(lista_contas)

        elif opcao_user == "3":
            if lista_contas:
                numero_conta =input("Digite o numero da conta para acessa-la: ")

                if numero_conta.isdigit():
                    for conta in self.contas:
                        if(conta.numero == int(numero_conta)):
                            print(f"\nConta acessada com número {conta.numero}".center(80))
                            conta.menu_conta()
                            self.menu_usuario(lista_contas)
                            break
                    else:
                        print("Numero da conta não encontrado".center(80))
                    
                else:
                    print("valor invalido".center(80))
            else:
                print("Sem contas cadastradas".center(80))
            
            self.menu_usuario(lista_contas)

        elif opcao_user == "4":
            print(" Dados do Usuario ".center(80))
            print(f"Nome: {self.nome}  \nCPF: {self.cpf} \nData Nascimento: {self.data_nascimento}  \nEndereço: {self.endereco} \nContas: {len(self.contas)} do usuario")
            
            self.menu_usuario(lista_contas)

        elif opcao_user == "5":
            return
        
        else:
            print("Opção Invalida".center(80))
            self.menu_usuario(lista_contas)

def menu_inicial():
    menu = """
 [1] Cadastrar usuario
 [2] acessar sua conta de usuario
 [0] sair

=> """ 
    return input(menu).strip()

def cadastrar_usuario(usuarios,/):
    cpf = input("Digite seu CPF apenas numeros: ")

    if not cpf.isnumeric() or (len(cpf) > 11 or len(cpf) < 11):
        print("CPF Invalido".center(80))
    else:
        usuario = Cliente.filtrar_usuarios(cpf,usuarios)
        if usuario:
            print("Usuario já cadastrado com esse CPF".center(80))
        else:
            nome = input("Digite seu nome: ")
            data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
            lista_data = data_nascimento.split("-")
            if len(lista_data) == 3:
                verificar_dia = (len(lista_data[0]) > 2 and not lista_data[0].isnumeric() and not len(lista_data[0]) < 2)
                verificar_mes = (len(lista_data[1]) > 2 and not lista_data[1].isnumeric() and not len(lista_data[1]) < 2)
                verificar_ano = (len(lista_data[2]) > 4 and not lista_data[2].isnumeric() and not len(lista_data[2]) < 4)
                if verificar_dia or verificar_mes or verificar_ano:
                    print("os valores da Data estão incorreto".center(80))
                    return
            else:    
                print("Data de nascimento invalida".center(80))
                return
                
            endereco = input("Digite seu endereco (logadouro - numero - bairro - cidade/sigla - estado): ")
            
            print("usuario cadastrado".center(80))
            pessoaFisica = PessoaFisica(cpf,nome.title(),data_nascimento,endereco)

            usuarios_cadastrados.append(pessoaFisica)

usuarios_cadastrados = []
contas_cadastradas = []
while True:

    opcao = menu_inicial()

    print()
    if opcao == "1":
        print(" Cadastrar usuario ".center(80,"-"))
        cadastrar_usuario(usuarios_cadastrados) 
    
    elif opcao == "2":
        if usuarios_cadastrados:
            print(" Acessar conta de Usuario".center(80,"-"))
            Cliente.mostrar_usuarios(usuarios_cadastrados)
            print()
            cpf = input("Digite o cpf do usuario para entrar: ")
            usuario = Cliente.filtrar_usuarios(cpf,usuarios_cadastrados)
            
            if usuario:
                usuario.menu_usuario(contas_cadastradas)
            
            else:
                print("Usuario não encontrado".center(80))
        else:
            print("Sem usuarios cadastrados".center(80))

    
    elif opcao == "0":
        break

    else:
        print("Opção invalida".center(80))
    
print("Programa finalizado".center(80))