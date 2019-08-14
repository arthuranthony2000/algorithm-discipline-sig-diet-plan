from controllers import read, delete, insert, cadastro
from datetime import datetime

action = lambda op, nomeUsuario: solicitarDieta(nomeUsuario) if op == '1' else visualizarDietas(nomeUsuario) if op == '2' else visualizarHistoricoAlimentar(nomeUsuario)


def visualizarHistoricoAlimentar(nomeUsuarioCliente):
    historicoAlimentar = read.readFileHistoricoAlimentar()
    try:
        if len(list(historicoAlimentar[nomeUsuarioCliente].keys())) > 0:
            print('''
                        # #################################################
                        # #############  HISTORICO ALIMENTAR    ###########
                        # #################################################
                        # #################################################            
                        ''')
            print('Você possui historico alimentar com:')
            for it in list(historicoAlimentar[nomeUsuarioCliente].keys()):
                print(it.replace(nomeUsuarioCliente, ''))
            nut = input("Insira o nome do nutricionista listado para visualizar historico alimentar:\n>>> ")
            try:
                for it in range(0, len(historicoAlimentar[nomeUsuarioCliente][nomeUsuarioCliente+nut]), 2):
                    print('Historico número: ', it+1)
                numeroHistorico = input("Insira o número do historico que você deseja:\n>>> ")
                try:
                    ha = historicoAlimentar[nomeUsuarioCliente][nomeUsuarioCliente + nut][int(numeroHistorico)-1]
                    print(10 * ' ' + "Nome da dieta: " + ha.getNome())
                    print(10 * ' ' + "Tipo da dieta: " + ha.getTipo())
                    print(10 * ' ' + "Prescrição da dieta: " + ha.getAlimentos())
                    print(10 * ' ' + "Periodo da dieta:",
                          ha.getPeriodo())
                except IndexError:
                    print("Código informado não consta no seu historico.")
                except ValueError:
                    print("Apenas números são aceitos no código do historico alimentar")
            except KeyError:
                print("Você não possui historico alimentar com o nutricionista especificado.")
        else:
            print('Você não possui historico alimentar.')
    except KeyError:
        print("Você não possui historico alimentar.")


def chatBox(nomeUsuarioCliente, nomeUsuarioNutricionista):
    print('''
            # #################################################
            # #############  BEM VINDO AO CHAT BOX  ###########
            # #################################################
            # #################################################            
            ''')
    dietasCadastradas = read.readFileDieta()
    print(dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].getConversaCliente())
    print(">>> (Digite go() para enviar a mensagem, exit() para sair do chatbox ou clear() para limpar a conversa")
    while True:
        msg = ''
        p = ''
        command = False
        while p != 'go()' and p != 'exit()':
            p = input(">>> ")
            msg += p + '\n'
            if p == 'clear()':
                dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].limparConversaCliente()
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].limparConversaCliente()
                insert.insertDieta(dietasCadastradas)
            if p == 'go()':
                command = True
        msg = msg.replace('go()', '').replace('exit()', '').replace('clear()', '')
        if command:
            if not msg.replace('\n', '').count(' ') == len(msg.replace('\n', '')):
                dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaCliente(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioCliente + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioCliente][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaNutricionista(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioCliente + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaCliente(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioCliente + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaNutricionista(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioCliente + ': ' + msg + '\n\n')
                insert.insertDieta(dietasCadastradas)
        else:
            break


def interface(nomeUsuario):
    while True:
        clientesCadastrados = read.readFileCliente()

        op = input('''
            # #################################################
            # #############  MENU  ############################
            # #################################################
            # ########### DIET PLAN ###########################
            # ########### Bem vindo {0}             
            # #################################################
            # ####### 1 - SOLICITAR NOVA DIETA ################
            # ####### 2 - VISUALIZAR DIETAS SOLICITADAS #######
            # ####### 3 - VISUALIZAR HISTORICO ALIMENTAR ######
            # ####### 4 - SAIR                          #######
            # #################################################
            \n>>> '''.format(clientesCadastrados[nomeUsuario].getNome()))
        if op == '4':
            break
        else:
            action(op, nomeUsuario)


def solicitarDieta(nomeUsuario):
    print("Escolha um dentre os nutricionistas listados:")
    nutricionistasCadastrados = read.readFileNutricionista()

    for nutricionista in nutricionistasCadastrados:
        if nutricionistasCadastrados[nutricionista].getDisponibilidade():
            print("Nome de Identificação: "+nutricionista, "- Nome: Doutor", nutricionistasCadastrados[nutricionista].getNome())
    print('\nDigite o nome de identificação do nutricionista que você deseja:')
    nomeUsuarioNutricionista = input(">>> ")
    if nomeUsuarioNutricionista not in list(nutricionistasCadastrados.keys()):
        print("O nutricionista informado não existe!.")
    else:
        cadastro.cadastrarDieta(nomeUsuario, nomeUsuarioNutricionista)


def visualizarDietas(nomeUsuario):
    dietasCadastradas = read.readFileDieta()
    try:
        for dieta in dietasCadastradas[nomeUsuario]:
            print(dieta.replace(nomeUsuario, 'Dieta feito com o Doutor: '))
        nomeUsuarioNutricionista = input("Informe o nome de identificação do nutricionista para visualizar a dieta\n>>> ")
        if nomeUsuario+nomeUsuarioNutricionista in list(dietasCadastradas[nomeUsuario].keys()):
            if dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getConfirmacaoNutricionista() == 'False':
                print("O nutricionista não aceitou sua solicitação!.")
                delete.deletarDieta(nomeUsuario, nomeUsuarioNutricionista)
            elif dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getNome() == '' and dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getConfirmacaoNutricionista() == 'None':
                print("O Doutor "+nomeUsuarioNutricionista+" ainda não visualizou ou não definiu nada sobre a sua dieta, aguarde a resposta!.")
            elif dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getConfirmacaoCliente() == 'None':
                print(10 * ' ' + "Nome da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getNome())
                print(10 * ' ' + "Tipo da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getTipo())
                print(10 * ' ' + "Prescrição da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getAlimentos())
                print(10 * ' ' + "Periodo da dieta:",
                      dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getPeriodo())
                print(10 * ' ' + "Preço:",
                      dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getPreco())
                confirmacao = input("Você aceita essa dieta?: (s/N)\n>>> ").lower()
                if confirmacao == 's':
                    dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].setConfirmacaoCliente('True')
                    dietasCadastradas[nomeUsuarioNutricionista][nomeUsuario + nomeUsuarioNutricionista].setConfirmacaoCliente('True')
                    insert.insertDieta(dietasCadastradas)
                else:
                    dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].setConfirmacaoCliente('False')
                    dietasCadastradas[nomeUsuarioNutricionista][nomeUsuario + nomeUsuarioNutricionista].setConfirmacaoCliente(
                        'False')
                    insert.insertDieta(dietasCadastradas)
            else:
                print(10*' '+"Nome da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getNome())
                print(10*' '+"Tipo da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getTipo())
                print(10*' '+"Prescrição da dieta: " + dietasCadastradas[nomeUsuario][
                    nomeUsuario + nomeUsuarioNutricionista].getAlimentos())
                print(10*' '+"Periodo da dieta:",
                      dietasCadastradas[nomeUsuario][nomeUsuario + nomeUsuarioNutricionista].getPeriodo())
                chat = input("Você deseja acessar o chatBox? (s/N)\n>>> ").lower()
                if chat == 's':
                    chatBox(nomeUsuario, nomeUsuarioNutricionista)
        else:
            print("Você não possui nenhuma dieta com o nutricionista especificado")
    except KeyError:
        print("Você não solicitou nenhuma dieta!.")


