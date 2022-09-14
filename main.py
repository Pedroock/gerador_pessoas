# Um gerador de pessoas que terá nome completo, idade, cpf, naturalidade
import random, requests, regex, lxml, os, pathlib, psycopg2
from bs4 import BeautifulSoup


def gerador_nome(quantidade, nome_duplo=True):
    # Só escolhe um nome e sobrenome, tendo certeza que os sobrenomes não se repitam
    lista_sobrenomes = []
    lista_nomes = []
    # Pegando info da wikipedia
    link = requests.get('https://pt.wikipedia.org/wiki/Lista_de_prenomes_mais_comuns_no_Brasil').text
    soup = BeautifulSoup(link, 'lxml')
    wiki = soup.find('div', class_='mw-parser-output').find('tbody')
    bruto_nomes = regex.findall(r'<b>.*</b>', str(wiki))
    # Limpando os nomes
    for nome_bruto in bruto_nomes:
        nome_bruto = str(nome_bruto)
        nome_bruto = nome_bruto.replace('<b>', '').replace('<br/>', '').replace('</b>', '').split()
        nome = nome_bruto[0]
        lista_nomes.append(nome)
    # Pegando info da wikipedia
    link = requests.get('https://pt.wikipedia.org/wiki/Categoria:Sobrenomes_da_l%C3%ADngua_portuguesa').text
    soup = BeautifulSoup(link, 'lxml')
    wiki = soup.find('div', class_='mw-category mw-category-columns')
    bruto_sobrenomes = regex.findall(r'title=".*\b', str(wiki))
    # Limpando
    for sobrenome_bruto in bruto_sobrenomes:
        sobrenome_bruto = str(sobrenome_bruto)
        sobrenome_bruto = sobrenome_bruto.replace('title="', '').replace('">', ' ').split()
        sobrenome = sobrenome_bruto[0]
        lista_sobrenomes.append(sobrenome)
    # Começo da lista final
    lista_nomes_completos = []
    for x in range(quantidade):
        primeiro_nome = random.choice(lista_nomes)
        primeiro_sobrenome = random.choice(lista_sobrenomes)
        while True:
            segundo_sobrenome = random.choice(lista_sobrenomes)
            if segundo_sobrenome != primeiro_sobrenome:
                break
        # Só ativado de nome_duplo=True, adiciona noms composto, ta desativado por gerar nomes peculiares
        if nome_duplo:
            while True:
                segundo_nome = random.choice(lista_nomes)
                if segundo_nome != primeiro_nome:
                    break
            nome_completo = str(fr"{primeiro_nome} {segundo_nome} {primeiro_sobrenome} {segundo_sobrenome}")
            lista_nomes_completos.append(nome_completo)
        else:
            nome_completo = str(f"{primeiro_nome} {primeiro_sobrenome} {segundo_sobrenome}")
            lista_nomes_completos.append(nome_completo)
    return lista_nomes_completos


def gerador_idade(quantidade):
    """A ideia é criar um gerador de idade que leva em conta o percentual de população por idade, levando em conta
    levando em conta a pirâmide etária, as porcentagens são: 15,2%(0-9), 17,9%(10-19), 17,9%(20-29), 15,4%(30-39),
    13%(40-49), 9,6%(50-59), 6%(60-69), 3,4%(70-79), 1,4%(80-89), 0,2%(90-99)
    Somente contarão os +18"""
    lista_idades = []
    numerais = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    porcentagens = [15.2, 17.9, 17.9, 15.4, 13, 9.6, 6, 3.4, 1.4, 0.2]
    for x in range(quantidade):
        while True:
            primeiro_digito = random.choices(numerais, porcentagens, k=1)
            segundo_digito= random.choice(numerais)
            idade = int(str(primeiro_digito[0])+str(segundo_digito))
            if idade >= 18:
                break
        lista_idades.append(idade)
    return lista_idades


def gerador_cpf(quantidade):
    """Gera um CPF válido"""
    lista_cpfs = []
    numerais = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    multiplicador = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for a in range(quantidade):
        while True:
            sequência = random.choices(numerais, k=11)
            primeiro_digito = sequência[9]
            segundo_digito = sequência[10]
            primeira_soma = 0
            segunda_soma = 0
            # Primeira etapa
            for x, y in zip(multiplicador[1:], sequência[0:9]):
                primeira_soma += x * y
            if primeira_soma % 11 == primeiro_digito or (primeira_soma % 11 == 10 and primeiro_digito == 0):
                # Segunda etapa
                for x, y in zip(multiplicador, sequência[0:10]):
                    segunda_soma += x * y
                if segunda_soma % 11 == segundo_digito or (primeira_soma % 11 == 10 and primeiro_digito == 0):
                    cpf = (''.join(str(item) for item in sequência))
                    cpf = str(f'{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.'
                              f'{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
                    lista_cpfs.append(cpf)
                    break
                else:
                    continue
            else:
                continue
    return lista_cpfs


def gerador_naturalidade(quantidade):
    """Aqui eu vou criar um dicionário com cidades e estados com 324 opcões de cidades com pelo menos 100mil habitantes
    e depois eu devolvo uma lista aleatória com um número dessas cidades"""
    # Pegando info da wikipedia
    dicionario_cidade_estado = {'cidade': [], 'estado': []}
    link = requests.get(
        'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_acima_de_cem_mil_habitantes').text
    soup = BeautifulSoup(link, 'lxml')
    wiki = soup.find('table', class_='wikitable sortable').find('tbody')
    # Se
    for tr in wiki:
        tr = str(tr)
        cidade_estado = regex.findall(r'title="([^"]*)"', tr)
        if cidade_estado:
            cidade = str(cidade_estado[0])
            estado = str(cidade_estado[1])
            # Removendo redundâncias
            if ' (estado)' in estado:
                estado = estado.replace(' (estado)', '')
            elif ' (Brasil)' in estado:
                estado = estado.replace(' (Brasil)', '')
            if f' ({estado})' in cidade:
                cidade = cidade.replace(f' ({estado})', '')
            dicionario_cidade_estado['cidade'].append(cidade)
            dicionario_cidade_estado['estado'].append(estado)
    """Esse código ta funcionando para todas cidades da lista, menos Chapecó e Patos, onde essas aparecem como
    cidade e estado, então eu vou removê-las.
    Também estou tirando a primeira linha, porque ela não faz parte da lista"""
    del dicionario_cidade_estado['cidade'][0]
    del dicionario_cidade_estado['estado'][0]
    del dicionario_cidade_estado['cidade'][136]
    del dicionario_cidade_estado['estado'][136]
    del dicionario_cidade_estado['cidade'][293]
    del dicionario_cidade_estado['estado'][293]
    # Gerar a lista
    lista_cidades_estados = []
    for a in range(quantidade):
        num = random.randrange(0, 324)
        str_cidade_estado = f'{dicionario_cidade_estado["cidade"][num]}, {dicionario_cidade_estado["estado"][num]}'
        lista_cidades_estados.append(str_cidade_estado)
    return lista_cidades_estados


def gerador_dicionario(quantidade, nome_duplo=False):
    dicionário = {}
    if nome_duplo:
        nome = gerador_nome(quantidade, nome_duplo=True)
    else:
        nome = gerador_nome(quantidade)
    idade = gerador_idade(quantidade)
    cpf = gerador_cpf(quantidade)
    local = gerador_naturalidade(quantidade)
    dicionário['NOME'] = nome
    dicionário['IDADE'] = idade
    dicionário['CPF'] = cpf
    dicionário['NATURALIDADE'] = local
    return dicionário


def visualizador(dicionário):
    # Mostra o dicionário no terminal
    cor= {'R': '\033[1;35m', 'C': '\033[1;036m', 'ND': '\033[m'}
    print(f'{cor["R"]}NOME{cor["ND"]}  {cor["C"]}IDADE{cor["ND"]}  '
          f'{cor["R"]}CPF{cor["ND"]}  {cor["C"]}NATURALIDADE{cor["ND"]}')
    nome, idade, cpf, local = dicionário['NOME'], dicionário['IDADE'], dicionário['CPF'], dicionário['NATURALIDADE']
    for x in range(len(dicionário['NOME'])):
        print(f'{cor["R"]}{nome[x]}{cor["C"]}  {cor["C"]}{idade[x]}{cor["C"]}'
              f'  {cor["R"]}{cpf[x]}{cor["C"]}  {cor["C"]}{local[x]}{cor["ND"]}')


def arquivo_txt(dicionário):
    # Cria um arquivo txt no desktop
    desktop = pathlib.Path.home() / 'Desktop' / 'gerador.txt'
    with open(desktop, 'w+') as f:
        f.truncate()
        f.write('NOME, IDADE, CPF, NATURALIDADE\n')
        nome, idade, cpf, local = dicionário['NOME'], dicionário['IDADE'], dicionário['CPF'], dicionário['NATURALIDADE']
        for x in range(len(dicionário['NOME'])):
            f.write(f'{nome[x]}, {idade[x]}, {cpf[x]}, {local[x]}\n')


def adicionar_database(dicionário, dbname, user, host, password):
    # Joga os dados para uma database postgresql
    conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=password)
    with conn:
        c = conn.cursor()
        # Exclui a table atual e cria uma nova
        c.execute("""DROP TABLE IF EXISTS pessoas;
        create table pessoas(NOME VARCHAR, IDADE VARCHAR, CPF VARCHAR, NATURALIDADE VARCHAR)""")
        # Adiciona informação para a table
        nome, idade, cpf, local = dicionário['NOME'], dicionário['IDADE'], dicionário['CPF'], dicionário['NATURALIDADE']
        for x in range(len(dicionário['NOME'])):
            c.execute("INSERT INTO pessoas values(%s, %s,%s, %s)", (nome[x], idade[x], cpf[x], local[x]))
