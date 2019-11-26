import datetime

class Historico:

    def __init__(self):
        self.__data_abertura = datetime.datetime.today()
        self.__transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.__data_abertura))
        print("transações: ")
        for t in self.__transacoes:
            print("-", t)
    
    def get_data_abertura(self):
        return self.__data_abertura

    def get_transacoes(self):
        return self.__transacoes

    def set_transacoes(self, transacoes):
        self.__transacoes.append(transacoes)

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = saldo
        self.__limite = limite
        self.__historico = Historico()

    def get_historico(self):
        return self.__historico.imprime()

    def get_saldo(self):
        return self.__saldo
    
    def get_numero(self):
        return self.__numero

    def set_saldo(self, saldo):
        self.__saldo = saldo        

    def get_titular(self):
        return self.__titular

    def __str__(self):
        return self.__numero

    def deposita(self, valor):
        self.__valor = valor
        self.__saldo += valor
        self.__historico.set_transacoes("depósito de {}".format(valor))

    def saca(self, valor):
        if (self.__saldo < valor):
            print("Não há posibilidade de saque")
            return False
        else:
            print("Pode sacar: " +str(valor))
            self.__valor = valor
            self.__saldo -= valor
            self.__historico.set_transacoes("saque de {}".format(valor))

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.__numero, self.__saldo))
        self.__historico.set_transacoes("tirou extrato - saldo de {}".format(self.__saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            print("Não há posibilidade de transferência")
            return False
        else:
            print("Arrocha pode transferir")
            destino.deposita(valor)
            self.__historico.set_transacoes("transferencia de {} para conta {}".format(valor,destino))
            return True

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4', cliente1, 1000.0)
conta2 = Conta('123-5', cliente2, 1000.0)

conta1.deposita(100.0)
conta1.extrato()
conta1.saca(50.0)
conta1.extrato()
conta1.transfere_para(conta2, 200.0)
conta1.extrato()
conta2.extrato()
print("historico")
conta1.get_historico()
conta2.get_historico()
"""


conta2.extrato()
"""