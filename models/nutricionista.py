from models.pessoa import Pessoa


class Nutricionista(Pessoa):
    def __init__(self, nome, idade, sexo, nomeUsuario):
        super(Nutricionista, self).__init__(nome, idade, sexo, nomeUsuario)
        self.__classificao = []
        self.__disponibilidade = True

    def getClassificacao(self):
        return sum(self.__classificao)/len(self.__classificao)

    def setClassificacao(self, classficacao):
        self.__classificao.append(classficacao)

    def getDisponibilidade(self):
        return self.__disponibilidade

    def setDisponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade