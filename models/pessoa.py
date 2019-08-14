class Pessoa(object):
    def __init__(self, nome, idade, sexo, nomeUsuario):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__nomeUsuario = nomeUsuario

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = sexo

    def getNomeUsuario(self):
        return self.__nomeUsuario

    def setNomeUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario