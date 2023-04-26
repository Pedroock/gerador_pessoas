# Faz uma inerface para interagir com as funções do gerador
import main


while True:
    # Main
    print(f'Esse é o GERADOR DE PESSOAS')
    print('Você pode:')
    print(f'[1] Gerar informações em conjunto')
    print(f'[2] Gerar informações separadas')
    print(f'[3] Fechar o programa')
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
                print(f'[1] Vizualizar no terminal')
                print(f'[2] Criar um .txt com as informações')
                print(f'[3] Adicionar uma informação a uma database PostgreSQL')
                print(f'[4] Voltar ao menu principal')
                resposta_dicionário = input('Você deseja? ')
                if str(resposta_dicionário) == '1':
                    main.visualizador(dicionário)
                    print('=-'*25)
                elif str(resposta_dicionário) == '2':
                    main.arquivo_txt(dicionário)
                    print('-='*25)
                    print(f'O ARQUIVO FOI GERADO NO SEU DESKTOP')
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
                        print(f"Houve um erro")
                        print('=-'*25)
                    else:
                        print('-='*25)
                        print(f'Sucesso')
                        print('=-'*25)
                elif str(resposta_dicionário) == '4':
                    print('-='*25)
                    break
                else:
                    print(f'=RESPOSTA INVÁLIDA')
        else:
            print(f'=RESPOSTA INVÁLIDA')
    elif resposta_main == '2':
        # Separadas
        while True:
            print('Você pode')
            print(f'[1] Criar uma lista de NOMES')
            print(f'[2] Criar uma lista de IDADES')
            print(f'[3] Criar uma lista de CPFs')
            print(f'[4] Criar uma lista de CIDADES')
            print(f'[5] Voltar ao menu principal')
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
                        print(f'=RESPOSTA INVÁLIDA')
                else:
                    print(f'=RESPOSTA INVÁLIDA')
            if resposta_separadas == '1':
                print('-='*25)
                nomes = main.gerador_nome(quantidade)
                print(f'NOME')
                for nome in nomes:
                    print(f'{nome}')
                print('-='*25)
            if resposta_separadas == '2':
                print('-='*25)
                idades = main.gerador_idade(quantidade)
                print(f'IDADE')
                for idade in idades:
                    print(f'{idade}')
                print('-='*25)
            if resposta_separadas == '3':
                print('-='*25)
                cpfs = main.gerador_cpf(quantidade)
                print(f'CPF')
                for cpf in cpfs:
                    print(f'{cpf}')
                print('-='*25)
            if resposta_separadas == '4':
                print('-='*25)
                cidades = main.gerador_naturalidade(quantidade)
                print(f'CIDADE')
                for cidade in cidades:
                    print(f'{cidade}')
                print('-='*25)
            if resposta_separadas == '5':
                print('-='*25)
                break
    elif resposta_main == '3':
        break
    else:
        print(f'=RESPOSTA INVÁLIDA')
        print('-='*25)