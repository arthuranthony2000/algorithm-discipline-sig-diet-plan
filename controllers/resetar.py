import pickle


def resetarHistoricoAlimentar():
    arquivoHistoricoAlimentar = open('database/historico.dat', 'wb')
    pickle.dump({}, arquivoHistoricoAlimentar)
    arquivoHistoricoAlimentar.close()


def resetarUsuario():
    arquivoDeUsuarios = open('database/usuario.dat', 'wb')
    pickle.dump({}, arquivoDeUsuarios)
    arquivoDeUsuarios.close()


def resetarCliente():
    arquivoDeClientes = open('database/cliente.dat', 'wb')
    pickle.dump({}, arquivoDeClientes)
    arquivoDeClientes.close()


def resetarNutricionista():
    arquivoDeNutricionistas = open('database/nutricionista.dat', 'wb')
    pickle.dump({}, arquivoDeNutricionistas)
    arquivoDeNutricionistas.close()


def resetarDieta():
    arquivoDeDietas = open('database/dieta.dat', 'wb')
    pickle.dump({}, arquivoDeDietas)
    arquivoDeDietas.close()


def resetarTudo():
    resetarHistoricoAlimentar()
    resetarCliente()
    resetarNutricionista()
    resetarUsuario()
    resetarDieta()