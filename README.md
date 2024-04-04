# Criando um Sistema Bancário em Python

Desafio da criação de um programa para um Sistema Bancário desenvolvido em Python por Linha de Comando (CMD) para
o Bootcamp de **Python AI Backend Developer** da [Digtal Innovation One](https://www.dio.me/) (DIO).

## Desafio

Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem **Python**. Para a
primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.


- **Operação de depósito**

    Deve ser póssivel depositar valores positivos para a minha
    conta bancária. A v1 do projeto trabalha apenas com 1 usuario,
    dessa forma não precisamos nos preocupar em identifcar qual 
    é o número da agência e conta bancária. Todos os depósitos
    devem ser armazenados em uma variável e exibidos na 
    operação de extrato 

- **Operação de saque**

    O sistema deve permitir realizar 3 saques diários com limite
    máximo de R$ 500,00 por saque. Caso o usuário não tenha
    saldo em conta, o sistema deve exibir uma mensagem
    informando que não será possíve sacar o dinheiro por falta de
    saldo. Todos os saques devem ser armazenados em uma variável e
    exibidos na operação de extrato.

- **Operação de extrato**
    Essa operação deve listar todos os depósitos e saques
    realizados na conta. No fim da listagem deve ser exibido o 
    saldo atual da conta.
    Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Desafio 2

Precisamos deixar nosso códgio mais modularizado, para isso vamos
criar funções para as operações existentes: **sacar**, **depositar** e **visualizar extrato**. Além disso, para a versão 2 do nosso sistema
precisamos criar duas novas funções: **criar usuário** (cliente do banco)
e **criar conta corrente** (vincular com usuário).

### Melhorias

Separado as ações de saque, depósito e extrato em funções.
Criar duas novas funções: 
cadastrar usuário (cliente) e cadastrar conta bancária 
, opcional adicionar mais funções ex: listar contas, listar usuario. 
As contas criadas podem ser acessadas através do CPF do usuario, e as contas bancarias são acessadas pelo seu numero da conta que e sequencial,
cada conta também possui seu próprio saldo, e seu proprio extrato.


 - **Saque** <br>
    A função saque deve receber os argumentos apenas por nome **(keyword only)**. Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
 
 - **Depósito** <br>
    A função depósito deve receber os argumentos apenas por posição **(positional only)**. Sugestão de argumentos: saldo, valor, extrato.
    Sugestão de retorno: saldo e extrato.

 - **Extrato** <br>
    A função extrato deve receber os argumetnos por posição e nome **(positional only e keyword onlu=y)**. Argumentos posicionai: saldo, argumetos nomeados: extrato

 - **Criar usuário (cliente)** <br>
    O programa deve armazenar os usuários em uma lista, um usuário é composto por:`nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logadouro, numero - bairo - ciade/sigla estado`. Deve ser armazenado somento os números do CPF. Não podemos cadastrar 2 usuário com o mesmo CPF.

 - **Criar conta corrente** <br>
    O programa deve armazenar contas em uma lista, uma conta é composto por: `agência, número da conta e usuário. O número da conta é sequencial, inciando em 1`. O numero da agência e fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertecne a somete um usuário.

## 🔗 Referências
 - [Respositorio Trilha Python DIO](https://github.com/digitalinnovationone/trilha-python-dio)

 - [Desafio finalizado](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)
