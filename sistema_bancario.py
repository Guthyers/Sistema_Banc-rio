from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, edereco):
        self.edereco = edereco
        self.conta = []

    def realizar_transacao (self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta (self, conta):
        self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
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
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! voçe não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n@@@ Saque realizado com sucesso! @@@")
        else:
            print(("\n @@@ operação inválida @@@"))

        return False
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n @@@ Deposito realizado com sucesso! @@@")
        else:
            print("\n @@@ Sua operação falhou, o valor informado é invalido. @@@")
        
        return True
#parei aqui
class ContaCorrente(Conta):
    pass
class Historico:
    pass
class Transação(ABC):
    pass
class Saque(Transação):
    pass
class Deposito(Transação):
    pass