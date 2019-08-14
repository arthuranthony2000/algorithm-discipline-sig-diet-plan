from controllers import read, insert


def deletarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista):
    dietasCadastradas = read.readFileDieta()
    insert.insertHistorioAlimentar(nomeUsuarioCliente, nomeUsuarioNutricionista)
    del dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista]
    del dietasCadastradas[nomeUsuarioNutricionista][nomeUsuarioCliente + nomeUsuarioNutricionista]
    insert.insertDieta(dietasCadastradas)