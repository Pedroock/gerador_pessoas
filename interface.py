# Faz uma inerface para interagir com as funções do gerador
import main


cor = {'vd': '\033[1;32m', 'vm': '\033[1;31m', 'a': '\033[1;34m', 'l': '\033[m'}
while True:
    # Main
    print(f'Esse é o {cor["a"]}GERADOR DE PESSOAS{cor["l"]}')
    print('Você pode:')
    print(f'{cor["vd"]}[1]{cor["l"]} Gerar informações em conjunto')
    print(f'{cor["vd"]}[2]{cor["l"]} Gerar informações separadas')
    print(f'{cor["vd"]}[3]{cor["l"]} Fechar o programa')
    resposta_main = str(input('Você deseja? ')).strip()
    print('-='*25)
    if resposta_main == '1':
        # Conjunto
        resposta_conjunto = input('Você quer criar quantas pessoas? ')
        print('=-'*25)
        if isinstance(int(resposta_conjunto), int):
            # Cria o dicionário
            dicionário = main.gerador_dicionario(int(resposta_conjunto))
            while True:
                # Ação dicionário
                print('As informações foram geradas, você pode:')
                print(f'{cor["vd"]}[1]{cor["l"]} Vizualizar no terminal')
                print(f'{cor["vd"]}[2]{cor["l"]} Criar um .txt com as informações')
                print(f'{cor["vd"]}[3]{cor["l"]} Adicionar uma informação a uma database PostgreSQL')
                print(f'{cor["vd"]}[4]{cor["l"]} Voltar ao menu principal')
                resposta_dicionário = input('Você deseja? ')
                if str(resposta_dicionário) == '1':
                    main.visualizador(dicionário)
                    print('=-'*25)
                elif str(resposta_dicionário) == '2':
                    main.arquivo_txt(dicionário)
                    print('-='*25)
                    print(f'{cor["vd"]}O ARQUIVO FOI GERADO NO SEU DESKTOP{cor["l"]}')
                    print('=-'*25)
                elif str(resposta_dicionário) == '3':
                    print('-='*25)
                    dbname = str(input('Qual o nome da database? ')).strip()
                    user =  str(input('Qual o nome do usuário? ')).strip()
                    host = str(input('Qual o host? ')).strip()
                    password = str(input('Qual a senha? ')).strip()
                    try:
                        main.adicionar_database(dicionário, dbname, user, host, password)
                    except Exception:
                        print('-='*25)
                        print(f"{cor['vm']}Houve um erro{cor['l']}")
                        print('=-'*25)
                    else:
                        print('-='*25)
                        print(f'{cor["vd"]}Sucesso{cor["l"]}')
                        print('=-'*25)
                elif str(resposta_dicionário) == '4':
                    print('-='*25)
                    break
                else:
                    print(f'{cor["vm"]}RESPOSTA INVÁLIDA{cor["l"]}')
        else:
            print(f'{cor["vm"]}RESPOSTA INVÁLIDA{cor["l"]}')
    elif resposta_main == '2':
        # Separadas
        while True:
            print('Você pode')
            print(f'{cor["vd"]}[1]{cor["l"]} Criar uma lista de NOMES')
            print(f'{cor["vd"]}[2]{cor["l"]} Criar uma lista de IDADES')
            print(f'{cor["vd"]}[3]{cor["l"]} Criar uma lista de CPFs')
            print(f'{cor["vd"]}[4]{cor["l"]} Criar uma lista de CIDADES')
            print(f'{cor["vd"]}[5]{cor["l"]} Voltar ao menu principal')
            while True:
                resposta_separadas = str(input("Você deseja? ")).strip()
                if resposta_separadas == '5':
                    break
                else:
                    quantidade = input('Qual a quantidade? ').strip()
                if quantidade.isnumeric():
                    quantidade = int(quantidade)
                    if resposta_separadas == '1':
                        break
                    elif resposta_separadas == '2':
                        break
                    elif resposta_separadas == '3':
                        break
                    elif resposta_separadas == '4':
                        break
                    else:
                        print(f'{cor["vm"]}RESPOSTA INVÁLIDA{cor["l"]}')
                else:
                    print(f'{cor["vm"]}RESPOSTA INVÁLIDA{cor["l"]}')
            if resposta_separadas == '1':
                print('-='*25)
                nomes = main.gerador_nome(quantidade)
                print(f'{cor["a"]}NOME{cor["l"]}')
                for nome in nomes:
                    print(f'{cor["a"]}{nome}{cor["l"]}')
                print('-='*25)
            if resposta_separadas == '2':
                print('-='*25)
                idades = main.gerador_idade(quantidade)
                print(f'{cor["a"]}IDADE{cor["l"]}')
                for idade in idades:
                    print(f'{cor["a"]}{idade}{cor["l"]}')
                print('-='*25)
            if resposta_separadas == '3':
                print('-='*25)
                cpfs = main.gerador_cpf(quantidade)
                print(f'{cor["a"]}CPF{cor["l"]}')
                for cpf in cpfs:
                    print(f'{cor["a"]}{cpf}{cor["l"]}')
                print('-='*25)
            if resposta_separadas == '4':
                print('-='*25)
                cidades = main.gerador_naturalidade(quantidade)
                print(f'{cor["a"]}CIDADE{cor["l"]}')
                for cidade in cidades:
                    print(f'{cor["a"]}{cidade}{cor["l"]}')
                print('-='*25)
            if resposta_separadas == '5':
                print('-='*25)
                break
    elif resposta_main == '3':
        break
    else:
        print(f'{cor["vm"]}RESPOSTA INVÁLIDA{cor["l"]}')
        print('-='*25)