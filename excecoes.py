class VIException(Exception):
    def __init__(self, numero, valor, *args):
        self.__numero = numero
        self.__valor = valor        
        self.__mensagem = "Valor Inválido"
        super().__init__(*args)
    
    def print_mensagem_erro(self):
        print("{}: \nConta Nº {} \nValor {}.".format(self.__mensagem, self.__numero, self.__valor))

class SIException(Exception):
    def __init__(self, numero, saldo, valor, *args):
        self.__numero = numero
        self.__saldo = saldo
        self.__valor = valor
        self.__mensagem = "Saldo Insuficiente"
        super().__init__(*args)
        
    def print_mensagem_erro(self):
        print("{}: \nConta Nº {} \nSaldo {} \nValor {}.".format(self.__mensagem, self.__numero, self.__saldo, self.__valor))
        


class TJIException(Exception):
    def __init__(self, numero, taxa, *args):
        self.__numero = numero
        self.__taxa = taxa        
        self.__mensagem = "Taxa de Juros Inválida"
        super().__init__(*args)
    
    def print_mensagem_erro(self):
        print("{}: \nConta Nº {} \nTaxa {}.".format(self.__mensagem, self.__numero, self.__taxa))

class CIException(Exception):
    def __init__(self, numero, *args):
        self.__numero = numero
        self.__mensagem = "Conta Inexistente"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nConta Nº {}.".format(self.__mensagem, self.__numero))

class CEException(Exception):
    def __init__(self, numero, *args):
        self.__numero = numero
        self.__mensagem = "Conta Existente"
        super().__init__(*args)

    def print_mensagem_erro(self):
        print("{}: \nConta Nº {}.".format(self.__mensagem, self.__numero))