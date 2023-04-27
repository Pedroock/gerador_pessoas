![gerador](https://user-images.githubusercontent.com/103686624/234736765-c343c192-5132-4cf4-b2cf-d52558d628fd.jpg)
## Requerimentos
-Instale [Python](https://www.python.org/downloads/)</br>
-Instale [Microsoft Visual C++](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/), lembre de selecionar a opção "Desenvolvimento para desktop com C++"
</br>
![c++](https://user-images.githubusercontent.com/103686624/234313444-c1f7d5fc-53e4-4c63-84a1-25bf3b86f720.png)
</br>
-
-Usando **cmd.exe**, acesse a pasta da aplicação usadno `cd "pasta\da\aplicação"` e use o comando `pip install venv`. Agora podemos criar o virtual enviroment usando
o comando `py -m venv venv` e ativá-lo usando `"pasta\da\aplicação"\venv\Scripts\Activate.bat`. Por fim, use `pip install -r requirements.txt` para instalar as packages e
`py interface.py` para iniciar a aplicação. 
# Sobre
Esse projeto foi criado com o fim de aplicar conhecimentos sobre o Web Scraping, nesse caso foi utilizado o Beautiful Soup para acessar coletar dados da Wikipedia. Aqui 
vão ser criados modelos com:
<br>
**-NOME:** Uma junção de um nome e dois sobrenomes, onde ambos são tirados das listas de nomes mais comuns no Brasil da Wikipedia. </br>
**-IDADE:** Uma idade de 18 a 99 gerada com porcentagens de modo que a distribuição de idades em uma lista fique semelhante a pirâmide etária brasileira. </br>
**-CPF:** Um CPF válido aleatório.  </br>
**-NATURALIDADE:** Uma junção aleatória de uma cidade tirada da lista de cidades mais populosas do Brasil na Wikipedia e um estado aleatório.  </br>
