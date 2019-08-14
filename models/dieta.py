class Dieta(object):
    def __init__(self, nomeUsuarioCliente, nomeUsuarioNutricionista, tipoDieta):
        self.__nomeUsuarioCliente = nomeUsuarioCliente
        self.__nomeUsuarioNutricionista = nomeUsuarioNutricionista
        self.__nomeDieta = ''
        self.__tipoDieta = tipoDieta
        self.__alimentos = ''
        self.__preco = 0.0
        self.__periodo = 0
        self.__conversaCliente = ''
        self.__conversaNutricionista = ''
        self.__confirmacaoCliente = 'None'
        self.__confirmacaoNutricionista = 'None'

    def getNome(self):
        return self.__nomeDieta

    def setNome(self, nomeDieta):
        self.__nomeDieta = nomeDieta

    def getTipo(self):
        return self.__tipoDieta

    def setTipo(self, tipoDieta):
        self.__tipoDieta = tipoDieta

    def getAlimentos(self):
        return self.__alimentos

    def setAlimentos(self, alimentos):
        self.__alimentos = alimentos

    def getPreco(self):
        return self.__preco

    def setPreco(self, preco):
        self.__preco = preco

    def getPeriodo(self):
        return self.__periodo

    def setPeriodo(self, periodo):
        self.__periodo = periodo

    def getConfirmacaoCliente(self):
        return self.__confirmacaoCliente

    def setConfirmacaoCliente(self, confirmacaoCliente):
        self.__confirmacaoCliente = confirmacaoCliente

    def getConfirmacaoNutricionista(self):
        return self.__confirmacaoNutricionista

    def setConfirmacaoNutricionista(self, confirmacaoNutricionista):
        self.__confirmacaoNutricionista = confirmacaoNutricionista

    def limparConversaCliente(self):
        self.__conversaCliente = ''

    def limparConversaNutricionista(self):
        self.__conversaNutricionista = ''

    def getConversaCliente(self):
        return self.__conversaCliente

    def setConversaCliente(self, conversaCliente):
        self.__conversaCliente += conversaCliente

    def getConversaNutricionista(self):
        return self.__conversaNutricionista

    def setConversaNutricionista(self, conversaNutricionista):
        self.__conversaNutricionista += conversaNutricionista