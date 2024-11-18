print('---------Bem vindo a empresa Lucas Aparecido Rodolfi---------')
lista_funcionarios = [] #Lista para armazenar funcionários cadastrados.
id_global = 4909 

def cadastrar_funcionarios(id): #Função para cadastro de funcionários
    global id_global
    print('-' * 14 + 'MENU CADASTRAR FUNCIONÁRIO' + '-' * 14)
    nome = input('Entre com o nome do funcionário: ')
    setor = input('Entre com o setor do funcionário: ')
    salario = float(input('Entre com o salário do funcionário: '))
    print('-' * 54)
    
    funcionario = {
        'id': id_global,
        'Nome': nome,
        'Setor': setor,
        'Salário': salario
        }
    lista_funcionarios.append(funcionario.copy()) #Aqui adiciona funcionários dentro da lista.
    print(f"Funcionário cadastrado com sucesso! ID do funcionário: {id}")

def consultar_funcionarios(): #Função com menu para consultar funcionários cadastrados.
    while True:
        print('-' * 14 + 'MENU CONSULTAR FUNCIONÁRIO' + '-' * 14)
        print('1 - Consultar todos funcionário')
        print('2 - Consultar funcionário por id')
        print('3 - Consultar funcionário(s) por setor')
        print('4 - Retornar')
        print('-' * 54)
        menuConsulta = int(input('>> '))

        if menuConsulta == 1:
            for funcionario in lista_funcionarios:
                print(funcionario)
        elif menuConsulta == 2:
            id_consulta = int(input("Informe o id do funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario["id"] == id_consulta:
                    print(funcionario)
                    break
            else:
                print("Funcionário não encontrado.")
        elif menuConsulta == 3:
            setor_consulta = input("Informe o setor: ")
            for funcionario in lista_funcionarios:
                if funcionario["Setor"] == setor_consulta:
                    print(funcionario)
        elif menuConsulta == 4:
            return
        else:
            print("Opção inválida.")

def remover_funcionario(): #Função para remover funcionários .
    while True:
        print('-' * 15 + 'MENU REMOVER FUNCIONÁRIO' + '-' * 15)
        menuRemover = int(input('Digite o id do funcionário a ser removido: '))
        print('-' * 54)
        for funcionario in lista_funcionarios:
            if funcionario["id"] == menuRemover:
                lista_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso.")
                return
        else:
            print("Id inválido.")

while True: #Loop do menu principal.
    print('-' * 20 + 'MENU PRINCIPAL' + '-' * 20)
    print('1 - Cadastrar funcionários')
    print('2 - Consultar funcionário(s)')
    print('3 - Remover funcionários')
    print('4 - Sair')
    print('-' * 54)
    menuPrincipal = int(input('>> '))
    if menuPrincipal == 1:
        id_global += 1 
        cadastrar_funcionarios(id_global)
    elif menuPrincipal == 2:
        consultar_funcionarios()
    elif menuPrincipal == 3:
        remover_funcionario()
    elif menuPrincipal == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")




    
        
    

        












