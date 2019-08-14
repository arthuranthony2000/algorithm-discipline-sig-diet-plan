import pickle


def readFileCliente():
    arquivoDeClientes = open('database/cliente.dat', 'rb')
    clientesCadastrados = pickle.load(arquivoDeClientes)
    arquivoDeClientes.close()
    return clientesCadastrados


def readFileNutricionista():
    arquivoDeNutricionistas = open('database/nutricionista.dat', 'rb')
    nutricionistasCadastrados = pickle.load(arquivoDeNutricionistas)
    arquivoDeNutricionistas.close()
    return nutricionistasCadastrados


def readFileUsuario():
    arquivoDeUsuarios = open('database/usuario.dat', 'rb')
    usuariosCadastrados = pickle.load(arquivoDeUsuarios)
    arquivoDeUsuarios.close()
    return usuariosCadastrados


def readFileDieta():
    arquivoDeDietas = open('database/dieta.dat', 'rb')
    dietasCadastradas = pickle.load(arquivoDeDietas)
    arquivoDeDietas.close()
    return dietasCadastradas


def readFileHistoricoAlimentar():
    arquivoDeHistoricoAlimentar = open('database/historico.dat', 'rb')
    historicoAlimentar = pickle.load(arquivoDeHistoricoAlimentar)
    arquivoDeHistoricoAlimentar.close()
    return historicoAlimentar