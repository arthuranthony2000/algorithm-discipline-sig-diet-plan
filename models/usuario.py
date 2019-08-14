class Usuario(object):
    def __init__(self, nomeUsuario, senhaUsuario, tipoUsuario):
        self.__nomeUsuario = nomeUsuario
        self.__senhaUsuario = senhaUsuario
        self.__tipoUsuario = tipoUsuario
        self.__cadastroFisico = False

    def getNomeUsuario(self):
        return self.__nomeUsuario

    def setNomeUsuario(self, nomeUsuario):
        self.__nomeUsuario = nomeUsuario

    def getSenhaUsuario(self):
        return self.__senhaUsuario

    def setSenhaUsuario(self, senhaUsuario):
        self.__senhaUsuario = senhaUsuario

    def getTipoUsuario(self):
        return self.__tipoUsuario

    def setTipoUsuario(self, tipoUsuario):
        self.__tipoUsuario = tipoUsuario

    def getCadastroFisico(self):
        return self.__cadastroFisico

    def setCadastroFisico(self, cadastroFisico):
        self.__cadastroFisico = cadastroFisico

