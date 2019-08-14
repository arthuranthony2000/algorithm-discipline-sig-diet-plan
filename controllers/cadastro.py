from models.usuario import Usuario
from models.cliente import Cliente
from models.nutricionista import Nutricionista
from models.dieta import Dieta
from controllers import login
from controllers import read
from controllers import insert
from controllers import delete
import principal


def cadastrarUsuario():
    try:

        tipoUsuario = input("Tipo de usuário: \n1 - Cliente\n2 - Nutricionista\n>>> ")
        nomeUsuario = input("Insira um nome para o seu usuário (Sem acentos, pontuações, vírgulas e pontos!):\n>>> ")
        senhaUsuario = input("Insira uma senha para o seu usuário (Recomendável acima de 8 digitos com letras, números e simbolos)\n>>> ")
        assert nomeUsuario.isalpha() or senhaUsuario.isalnum()
        assert senhaUsuario.isalpha() or senhaUsuario.isalnum()

        usuariosCadastrados = read.readFileUsuario()

        if nomeUsuario in list(usuariosCadastrados.keys()):
            print('Esse usuário já existe!.')
            exit(principal.interface())

        usuariosCadastrados[nomeUsuario] = Usuario(nomeUsuario, senhaUsuario, tipoUsuario)

        insert.insertUsuario(usuariosCadastrados)

        cadastrarCliente(nomeUsuario) if tipoUsuario == '1' else cadastrarNutricionista(nomeUsuario)
    except AssertionError:
        print("Entradas inválidas.")


def cadastrarCliente(nomeUsuario):
    try:
        nome = input("Insira seu nome: \n>>> ")
        assert nome.replace(' ', '').isalpha()
        idade = int(input("Insira sua idade: \n>>> "))
        assert idade > 0
        sexo = input("Insira seu sexo:  \n1) Masculino \n2) Feminino\n>>> ")
        sexo = "Masculino" if sexo == '1' else "Feminino"
        peso = int(input("Insira seu peso: (em kg)\n>>> "))
        assert peso > 0
        altura = int(input("Insira sua altura: (em cm)\n>>> "))
        assert altura > 0
        nivelAtividadeFisica = input("Insira seu nível de atividade física: \n1) Sedentario \n2) Moderado \n3) Ativo\n>>> ")
        nivelAtividadeFisica = 'Ativo' if nivelAtividadeFisica == '3' else 'Moderado' if nivelAtividadeFisica == '2' else 'Sedentario'
        clientesCadastrados = read.readFileCliente()

        clientesCadastrados[nomeUsuario] = Cliente(nome, idade, sexo, peso, altura, nivelAtividadeFisica, nomeUsuario)
        clientesCadastrados[nomeUsuario].setTaxaMetabolicaBasal()
        clientesCadastrados[nomeUsuario].setIMC()

        insert.insertCliente(clientesCadastrados)

        usuariosCadastrados = read.readFileUsuario()

        usuariosCadastrados[nomeUsuario].setCadastroFisico(True)

        insert.insertUsuario(usuariosCadastrados)

        login.autenticacao(nomeUsuario, usuariosCadastrados[nomeUsuario].getSenhaUsuario())
    except ValueError:
        print("Entrada inválida")

    except AssertionError:
        print("Entrada inválida!.")


def cadastrarNutricionista(nomeUsuario):
    try:
        nome = input("Insira seu nome: \n>>> ")
        assert nome.replace(' ', '').isalpha()
        idade = int(input("Insira sua idade: \n>>> "))
        assert idade > 0
        sexo = input("Insira seu sexo:  \n1) Masculino \n2) Feminino\n>>> ")
        sexo = "Masculino" if sexo == '1' else "Feminino"

        nutricionistasCadastrados = read.readFileNutricionista()

        nutricionistasCadastrados[nomeUsuario] = Nutricionista(nome, idade, sexo, nomeUsuario)

        insert.insertNutricionista(nutricionistasCadastrados)

        usuariosCadastrados = read.readFileUsuario()

        usuariosCadastrados[nomeUsuario].setCadastroFisico(True)

        insert.insertUsuario(usuariosCadastrados)

        login.autenticacao(nomeUsuario, usuariosCadastrados[nomeUsuario].getSenhaUsuario())
    except ValueError:
        print("Entrada inválida!.")

    except AssertionError:
        print("Entradas inválidas.")


def cadastrarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista):
    dietasCadastradas = read.readFileDieta()

    if nomeUsuarioCliente not in list(dietasCadastradas.keys()):
        dietasCadastradas[nomeUsuarioCliente] = {}

    if nomeUsuarioNutricionista not in list(dietasCadastradas.keys()):
        dietasCadastradas[nomeUsuarioNutricionista] = {}

    if nomeUsuarioCliente+nomeUsuarioNutricionista in list(dietasCadastradas[nomeUsuarioCliente].keys()):
        print('Você já possui uma dieta com esse nutricionista!.')
        op = input("Deseja deletar a atual e criar uma nova? (s/N)\n>>> ").lower()
        if op == 's':
            insert.insertHistorioAlimentar(nomeUsuarioCliente, nomeUsuarioNutricionista)
            delete.deletarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista)
            cadastrarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista)

    else:
        tipoDieta = input("Informe o tipo de Dieta: \n1) - Emagrecer \n2) - Ganhar Massa Muscular  \n>>> ")
        tipoDieta = "Emagrecer" if tipoDieta == "1" else "Ganhar massa muscular."
        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista] = Dieta(nomeUsuarioCliente, nomeUsuarioNutricionista, tipoDieta)
        dietasCadastradas[nomeUsuarioNutricionista][nomeUsuarioCliente + nomeUsuarioNutricionista] = Dieta(nomeUsuarioCliente, nomeUsuarioNutricionista, tipoDieta)
        insert.insertDieta(dietasCadastradas)