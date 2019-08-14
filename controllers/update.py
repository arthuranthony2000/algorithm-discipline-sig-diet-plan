from controllers import read, insert


def alterarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista, idMudanca, valor):
    dietasCadastradas = read.readFileDieta()
    if idMudanca == '1':
        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].setNome(valor)
        dietasCadastradas[nomeUsuarioNutricionista][nomeUsuarioCliente + nomeUsuarioNutricionista].setNome(valor)
        insert.insertDieta(dietasCadastradas)
    elif idMudanca == '2':
        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].setAlimentos(valor)
        dietasCadastradas[nomeUsuarioNutricionista][nomeUsuarioCliente + nomeUsuarioNutricionista].setAlimentos(valor)
        insert.insertDieta(dietasCadastradas)
    else:
        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].setPeriodo(valor)
        dietasCadastradas[nomeUsuarioNutricionista][nomeUsuarioCliente + nomeUsuarioNutricionista].setPeriodo(valor)
        insert.insertDieta(dietasCadastradas)