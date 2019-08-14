from views import interfaceCliente, interfaceNutricionista
from controllers import read, cadastro


def autenticacao(nomeUsuario, senhaUsuario):
    usuariosCadastrados = read.readFileUsuario()

    try:
        if usuariosCadastrados[nomeUsuario].getSenhaUsuario() == senhaUsuario:
            if not usuariosCadastrados[nomeUsuario].getCadastroFisico():
                cadastro.cadastrarCliente(nomeUsuario) if usuariosCadastrados[nomeUsuario].getTipoUsuario() == '1' else cadastro.cadastrarNutricionista(
                    nomeUsuario)
            else:
                if usuariosCadastrados[nomeUsuario].getTipoUsuario() == '1':
                    interfaceCliente.interface(nomeUsuario)
                else:
                    interfaceNutricionista.interface(nomeUsuario)
            pass
        else:
            print("Senha incorreta!.")
    except KeyError:
        print("Esse usuário não existe!.")