from controllers import read, delete, insert, update
from datetime import datetime

action = lambda op, nomeUsuario: visualizarDietas(nomeUsuario) if op == '' else ''


def prescricao(msg):
    msg += '\n\n'+(20*'=')+'CARDÁPIO'+(20*'=')+'\n'
    refeicoes = ['CAFÉ DA MANHÃ', 'LANCHE DA MANHÃ', 'ALMOÇO', 'LANCHE DA TARDE', 'JANTAR', 'SEIA']
    for it in range(len(refeicoes)):
        print(refeicoes[it])
        msg += '\n'+(10*' ')+(10*'=')+f'{refeicoes[it]}'+(10*'=')+(10*' ')+'\n'
        horario = input(f'Informe o horário do {refeicoes[it]}: (XXh:YYmin)\n>>> ')
        msg += 'Horário: ' + horario + '\n'
        c = 1
        while c < 4:
            print(f'{c}ª OPÇÃO:')
            msg += '\n'+(10*' ')+f'{c}ª OPÇÃO:\n'
            p = ''
            while p != 'go()':
                p = input(">>> ")
                msg += p + '\n'
            c += 1
    return msg


def chatBox(nomeUsuarioCliente, nomeUsuarioNutricionista):
    print('''
            # #################################################
            # #############  BEM VINDO AO CHAT BOX  ###########
            # #################################################
            # #################################################            
            ''')
    dietasCadastradas = read.readFileDieta()
    print(dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].getConversaNutricionista())
    print(">>> (Digite go() para enviar a mensagem, exit() para sair do chatbox ou clear() para limpar a conversa")
    while True:
        msg = ''
        p = ''
        command = False
        while p != 'go()' and p != 'exit()':
            p = input(">>> ")
            msg += p + '\n'
            if p == 'clear()':
                dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].limparConversaNutricionista()
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].limparConversaNutricionista()
                insert.insertDieta(dietasCadastradas)
            if p == 'go()':
                command = True
        msg = msg.replace('go()', '').replace('exit()', '').replace('clear()', '')
        if command:
            if not msg.replace('\n', '').count(' ') == len(msg.replace('\n', '')):
                dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaCliente(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioNutricionista + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioCliente][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaNutricionista(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioNutricionista + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaCliente(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioNutricionista + ': ' + msg + '\n\n')
                dietasCadastradas[nomeUsuarioNutricionista][
                    nomeUsuarioCliente + nomeUsuarioNutricionista].setConversaNutricionista(
                    '- [' + str(datetime.now())[:-7] + '] ' + nomeUsuarioNutricionista + ': ' + msg + '\n\n')
                insert.insertDieta(dietasCadastradas)
        else:
            break


def alterarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista):
    print('''
                        # #################################################
                        # #####  O QUE VOCÊ DESEJA FAZER AGORA?. ##########
                        # #################################################
                        # #### 1) - ALTERAR NOME ##########################
                        # #### 2) - ALTERAR PRESCRIÇÃO      ###############
                        # #### 3) - ALTERAR PERIODO         ###############
                        # #### 4) - SAIR    ###############################
                        # #################################################
                        ''')
    op = input("\n>>> ")
    if op == '1':
        update.alterarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista, op, input("Insira um novo nome para a dieta:\n>>> "))
    elif op == '2':
        print(">>> (Digite go() para enviar a prescrição")
        msg = prescricao('')
        msg = msg.replace('go()', '')
        update.alterarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista, op, msg)
    elif op == '3':
        try:
            periodo = int(input("Insira um novo periodo para a dieta:\n>>> "))
            assert periodo > 0
            update.alterarDieta(nomeUsuarioCliente, nomeUsuarioNutricionista, op, periodo)
        except ValueError:
            print("Entrada inválida!.")
        except AssertionError:
            print("Valores númericos devem ser maiores que zero!.")


def interface(nomeUsuario):
    while True:
        nutricionistasCadastrados = read.readFileNutricionista()

        op = input('''
            # #################################################
            # #############  MENU  ############################
            # #################################################
            # ########### DIET PLAN ###########################
            # ########### Bem vindo {0}             
            # #################################################
            # #################################################
            # ####### ENTER - VISUALIZAR DIETAS SOLICITADAS ###
            # ####### 2 - SAIR                          #######
            # #################################################
            \n>>> '''.format(nutricionistasCadastrados[nomeUsuario].getNome()))
        if op == '2':
            break
        else:
            action(op, nomeUsuario)


def visualizarDietas(nomeUsuario):
    dietasCadastradas = read.readFileDieta()
    try:
        for dieta in dietasCadastradas[nomeUsuario]:
            print("Dieta solicitada por: "+dieta.replace(nomeUsuario, ''))
        nomeUsuarioCliente = input("Informe o nome de identificação do cliente para visualizar suas informações\n>>> ")
        if nomeUsuarioCliente in list(dietasCadastradas.keys()):
            if dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getConfirmacaoCliente() == 'False':
                print("O cliente não aceitou a proposta!.")
                delete.deletarDieta(nomeUsuarioCliente, nomeUsuario)
            elif dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getConfirmacaoNutricionista() == 'None':
                clientesCadastrados = read.readFileCliente()
                print(10 * ' ' + "Nome:", clientesCadastrados[nomeUsuarioCliente].getNome())
                print(10 * ' ' + "Idade:", clientesCadastrados[nomeUsuarioCliente].getIdade())
                print(10 * ' ' + "Sexo:", clientesCadastrados[nomeUsuarioCliente].getSexo())
                print(10 * ' ' + "Peso:", clientesCadastrados[nomeUsuarioCliente].getPeso())
                print(10 * ' ' + "Altura:", clientesCadastrados[nomeUsuarioCliente].getAltura())
                print(10 * ' ' + "IMC:", clientesCadastrados[nomeUsuarioCliente].getIMC())
                print(10 * ' ' + "Taxa Metabolica Basal:", clientesCadastrados[nomeUsuarioCliente].getTaxaMetabolicaBasal())
                print(10 * ' ' + "Nivel de Atividade Física:", clientesCadastrados[nomeUsuarioCliente].getNivelAtividadeFisica())
                print(10 * ' ' + "Tipo de dieta solicitada:",
                      dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getTipo())
                confirmacao = input("Você aceita essa dieta?: (s/N)\n>>> ").lower()
                if confirmacao == 's':
                    dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setConfirmacaoNutricionista('True')
                    dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setConfirmacaoNutricionista('True')
                    nome = input("Digite o nome da dieta:\n>>> ")
                    try:
                        preco = float(input("Digite o preço da dieta:\n>>> "))
                        dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setNome(nome)
                        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setNome(nome)
                        dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setPreco(preco)
                        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setPreco(preco)

                        insert.insertDieta(dietasCadastradas)
                    except ValueError:
                        print("Entrada inválida!.")

                else:
                    dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setConfirmacaoNutricionista('False')
                    dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setConfirmacaoNutricionista(
                        'False')
                    insert.insertDieta(dietasCadastradas)
            elif dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getConfirmacaoCliente() == 'None':
                print("O cliente está analisando a proposta!.")
            else:
                if dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getAlimentos() == '':
                    print("O cliente aceitou a proposta!.")
                    print("Você não definiu nenhuma prescrição, DEFINA!.")
                    print(">>> (Digite go() para enviar a prescrição")
                    msg = prescricao('')
                    msg = msg.replace('go()', '')
                    dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setAlimentos(msg)
                    dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setAlimentos(msg)
                    try:
                        periodo = int(input("Informe o periodo da dieta em meses!.\n>>> "))
                        assert periodo > 0
                        dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].setPeriodo(periodo)
                        dietasCadastradas[nomeUsuarioCliente][nomeUsuarioCliente + nomeUsuario].setPeriodo(periodo)
                        insert.insertDieta(dietasCadastradas)
                    except ValueError:
                        print("Entrada inválida!.")
                    except AssertionError:
                        print("Valores númericos devem ser maiores que zero!.")
                else:
                    clientesCadastrados = read.readFileCliente()
                    print(10 * ' ' + "Nome:", clientesCadastrados[nomeUsuarioCliente].getNome())
                    print(10 * ' ' + "Idade:", clientesCadastrados[nomeUsuarioCliente].getIdade())
                    print(10 * ' ' + "Sexo:", clientesCadastrados[nomeUsuarioCliente].getSexo())
                    print(10 * ' ' + "Peso:", clientesCadastrados[nomeUsuarioCliente].getPeso())
                    print(10 * ' ' + "Altura:", clientesCadastrados[nomeUsuarioCliente].getAltura())
                    print(10 * ' ' + "IMC:", clientesCadastrados[nomeUsuarioCliente].getIMC())
                    print(10 * ' ' + "Taxa Metabolica Basal:",
                          clientesCadastrados[nomeUsuarioCliente].getTaxaMetabolicaBasal())
                    print(10 * ' ' + "Nivel de Atividade Física:",
                          clientesCadastrados[nomeUsuarioCliente].getNivelAtividadeFisica())
                    print(10 * ' ' + "Tipo de dieta solicitada:",
                          dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getTipo())
                    print(10 * ' ' + "Nome da Dieta:", dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getNome())
                    print(10 * ' ' + "Prescrição:",
                          dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getAlimentos())
                    print(10 * ' ' + "Período:",
                          dietasCadastradas[nomeUsuario][nomeUsuarioCliente + nomeUsuario].getPeriodo())
                    print('''
                    # #################################################
                    # #####  O QUE VOCÊ DESEJA FAZER AGORA?. ##########
                    # #################################################
                    # #### 1) - ACESSAR CHAT BOX ######################
                    # #### 2) - ALTERAR DADOS DA DIETA      ###########
                    # #### 3) - SAIR    ###############################
                    # #################################################
                    ''')
                    op = input("\n>>> ")
                    if op == '1':
                        chatBox(nomeUsuarioCliente, nomeUsuario)
                    elif op == '2':
                        alterarDieta(nomeUsuarioCliente, nomeUsuario)

        else:
            print("Esse usuário não existe ou não solicitou dieta para você.")
    except KeyError:
        print("Nenhuma dieta solicitada!.")