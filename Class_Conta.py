class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    PI = 3.14 #esse é um exemplo de um atributo que funciona como se fosse um  método estático,
              #para o caso de esse método apenas retorna um valor, essa é uma aplicação útil.
              #esse atributo substituiu o seguinte método:
              # @staticmethod
              #  def obter_pi():
              #      return 3.14
              #para utilizar esse atributo basta: >>> from conta import Conta    >>> Conta.PI
            
#self é a referência do endereçamento da memória na qual foi alocada a classe.
#__init__ é a função construtura.

    def extrato(self):
        print("Saldo de R$ {} do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R$ {} passou o limite disponível.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #Existe a forma abaixo de usar getters e setters.
    #Aqui se chama o método da seguinte maneira -> conta.get_saldo(); conta.get_titular; conta.get_limite(); conta.set_limite(limite).


    #def get_saldo(self):
    #    return self.__saldo

    #def get_titular(self):
    #    return self.__titular

    #def get_limite(self):
    #    return self.__limite

    #def set_limite(self, limite):
    #    self.__limite = limite

    #E também existe a forma abaixo de usar getters (@property) e setters (@nome-do-método.setter).
    #Aqui se chama o método da seguinte forma -> conta.saldo; conta.titular; conta.limite; conta.limite = "valor".

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


#método estático é da classe e não do objeto, assim ele pode ser acessado/chamado mesmo sem a criação do objeto. E não manipula informações/atributos de objetos.
#para ilustrar: no console -> >>> from conta import Conta
                              #>>> Conta.codigo_banco()
                              #'001'

                              #>>> from conta import Conta
                              #>>> codigos = Conta.codigos_bancos()
                              #>>> codigos
                              #{'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
                              #>>> codigos['BB']
                              #'001'
                              #>>> codigos['Caixa']
                              #'104'

                              #Conta.codigos_bancos()['BB']
                              #'001'


    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
