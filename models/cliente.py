from models.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, peso, altura, nivelAtividadeFisica, nomeUsuario):
        super(Cliente, self).__init__(nome, idade, sexo, nomeUsuario)
        self.__peso = peso
        self.__altura = altura
        self.__nivelAtividadeFisica = nivelAtividadeFisica
        self.__taxaMetabolicaBasal = 0
        self.__IMC = 0

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

    def getNivelAtividadeFisica(self):
        return self.__nivelAtividadeFisica

    def setNivelAtividadeFisica(self, nivelAtividadeFisica):
        self.__nivelAtividadeFisica = nivelAtividadeFisica

    def getTaxaMetabolicaBasal(self):
        return self.__taxaMetabolicaBasal

    def setTaxaMetabolicaBasal(self):
        self.__taxaMetabolicaBasal = 66 + (13.7 * self.__peso) + (5.0 * self.__altura) - (6.8 * self.getIdade()) if self.getSexo() == 'Masculino' else 665 + (9.6 * self.__peso) + (5 * self.__altura) - (6.8 * self.getIdade())

    def getIMC(self):
        return self.__IMC

    def setIMC(self):
        self.__IMC = (int(self.__peso) / int(self.__altura) ** 2)*10000
