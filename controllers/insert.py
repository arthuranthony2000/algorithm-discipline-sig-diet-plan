import pickle
from controllers import read


def insertUsuario(usuariosCadastrados):
    arquivoDeUsuarios = open('database/usuario.dat', 'wb')
    pickle.dump(usuariosCadastrados, arquivoDeUsuarios)
    arquivoDeUsuarios.close()


def insertCliente(clientesCadastrados):
    arquivoDeClientes = open('database/cliente.dat', 'wb')
    pickle.dump(clientesCadastrados, arquivoDeClientes)
    arquivoDeClientes.close()


def insertNutricionista(nutricionistasCadastrados):
    arquivoDeNutricionistas = open('database/nutricionista.dat', 'wb')
    pickle.dump(nutricionistasCadastrados, arquivoDeNutricionistas)
    arquivoDeNutricionistas.close()


def insertDieta(dietasCadastradas):
    arquivoDeDietas = open('database/dieta.dat', 'wb')
    pickle.dump(dietasCadastradas, arquivoDeDietas)
    arquivoDeDietas.close()


def insertHistorioAlimentar(nomeUsuarioCliente, nomeUsuarioNutricionista):
    dietasCadastradas = read.readFileDieta()
    if dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente+nomeUsuarioNutricionista].getAlimentos() != '':
        historicoAlimentar = read.readFileHistoricoAlimentar()

        if nomeUsuarioCliente not in list(historicoAlimentar.keys()):
            historicoAlimentar[nomeUsuarioCliente] = {}

        if nomeUsuarioNutricionista not in list(historicoAlimentar.keys()):
            historicoAlimentar[nomeUsuarioNutricionista] = {}

        if nomeUsuarioCliente+nomeUsuarioNutricionista not in list(historicoAlimentar[nomeUsuarioCliente].keys()):
            historicoAlimentar[nomeUsuarioCliente][nomeUsuarioCliente+nomeUsuarioNutricionista] = []

        if nomeUsuarioCliente+nomeUsuarioNutricionista not in list(historicoAlimentar[nomeUsuarioNutricionista].keys()):
            historicoAlimentar[nomeUsuarioNutricionista][nomeUsuarioCliente+nomeUsuarioNutricionista] = []

        historicoAlimentar[nomeUsuarioCliente][nomeUsuarioCliente+nomeUsuarioNutricionista].append(dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente+nomeUsuarioNutricionista])
        historicoAlimentar[nomeUsuarioNutricionista][nomeUsuarioCliente+nomeUsuarioNutricionista].append(dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente+nomeUsuarioNutricionista])

        arquivoHistoricoAlimentar = open('database/historico.dat', 'wb')
        pickle.dump(historicoAlimentar, arquivoHistoricoAlimentar)
        arquivoHistoricoAlimentar.close()
    else:
        print("A dieta foi deletada, porém não foi cadastrada no seu historico pois não possuia prescrição.")