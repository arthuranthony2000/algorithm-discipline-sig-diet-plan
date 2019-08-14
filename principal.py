from controllers import login, cadastro

vrOP = lambda op: login.autenticacao(input("Insira o nome de usuário:\n>>> "), input("Insira a senha do usuário:\n>>> ")) if op == '1' else cadastro.cadastrarUsuario() if op == '2' else ''


def interface():
    while True:
        op = input('''
        ####################################
        #############  MENU  ###############
        ####################################
        ########### DIET PLAN ##############
        ####################################
        ####### 1 - LOGAR ##################
        ####### 2 - CADASTRO ###############
        ####### 3 - SAIR     ###############
        ####################################
        \n>>> ''')
        if op == '3':
            break
        else:
            vrOP(op)


if __name__ == '__main__':
    interface()