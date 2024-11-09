# Projeto Django

 Projeto Django - Geração de Combinações e Análise de Acertos para Jogos de Loteria

Este projeto é uma aplicação web desenvolvida com Django que gera combinações numéricas para jogos de loteria e realiza uma análise dos acertos em relação a resultados anteriores. Ele permite ao usuário visualizar as melhores combinações que mais acertaram 12, 13, 14 e 15 pontos em um conjunto de combinações geradas.
Funcionalidades

    Geração de Combinações: Gera combinações aleatórias de números com base nas dezenas mais sorteadas.
    Análise de Acertos: Analisa as combinações geradas e filtra as que mais acertaram em relação a um histórico de resultados anteriores.
    Visualização das Melhores Combinações: Exibe as melhores combinações para acertos de 12, 13, 14 e 15 pontos, permitindo uma análise detalhada.

Pré-requisitos

    Python 3.8+
    Django 3.2+
    Um arquivo .csv com o histórico de resultados anteriores, localizado na raiz do projeto.

Instalação e Execução

Siga os passos abaixo para instalar e executar o projeto em sua máquina local.
1. Clonar o Repositório

No terminal, execute o comando abaixo para clonar este repositório:

git clone https://github.com/leeofernandes1980/projeto_django.git
cd projeto_django

2. Criar e Ativar o Ambiente Virtual

Para isolar as dependências do projeto, crie um ambiente virtual e ative-o:

python -m venv venv
# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate
# No MacOS/Linux
source venv/bin/activate

3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

pip install -r requirements.txt

4. Configurar o Banco de Dados

O projeto utiliza SQLite como banco de dados padrão. Execute as migrações para criar as tabelas necessárias:

python manage.py migrate

5. Executar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento Django para testar a aplicação localmente:

python manage.py runserver

6. Acessar a Aplicação

Abra o navegador e acesse:

http://127.0.0.1:8000/gerar-combinacoes/

Isso carregará a página onde você poderá ver as combinações geradas e as melhores combinações para os acertos de 12, 13, 14 e 15 pontos.
Estrutura do Projeto

Mais detalhes para a execução do código:

Configuração e Execução do Projeto

Siga os passos abaixo para configurar e executar este projeto Django em sua máquina local.
1. Clone o Repositório

git clone https://github.com/seu_usuario/projeto_django.git
cd projeto_django

2. Crie e Ative um Ambiente Virtual

    Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

3. Instale as Dependências

Certifique-se de que todas as dependências do projeto estão instaladas:

pip install -r requirements.txt

4. Configure o Banco de Dados

Aplique as migrações do banco de dados para configurar as tabelas necessárias:

python manage.py migrate

5. Coloque o Arquivo CSV na Raiz do Projeto

Certifique-se de que o arquivo lotofacilatual1.csv com o histórico de resultados da Lotofácil esteja na raiz do projeto. O código foi configurado para buscar o arquivo nesse local:

projeto_django/
├── combinacoes/
├── projeto_django/
├── venv/
├── .gitignore
├── README.md
├── db.sqlite3
├── lotofacilatual1.csv  # <-- Coloque o arquivo CSV aqui
└── manage.py

6. Crie o Diretório static (opcional)

Para evitar avisos sobre arquivos estáticos, crie uma pasta static na raiz do projeto:

mkdir static

7. Inicie o Servidor de Desenvolvimento

Com o ambiente configurado, execute o servidor de desenvolvimento Django:

python manage.py runserver

8. Acesse a Aplicação

Abra o navegador e acesse o seguinte endereço para visualizar as combinações geradas:

http://127.0.0.1:8000/gerar-combinacoes/


    projeto_django/: Pasta principal do projeto Django, contendo configurações e arquivos principais.
    combinacoes/: Aplicação responsável por gerar as combinações e realizar a análise de acertos.
    templates/combinacoes/resultado.html: Template HTML para exibir os resultados das combinações e suas análises.
    lotofacilatual1.csv: Arquivo CSV com o histórico de resultados que será usado para a análise de acertos.

Personalização

    Alterar o número de combinações: O número de combinações geradas pode ser ajustado no código. No arquivo views.py, altere o valor de num_combinacoes na função gerar_combinacoes_view para definir quantas combinações devem ser geradas.
    Atualizar o arquivo de resultados: Substitua o lotofacilatual1.csv pelo seu próprio arquivo de histórico de resultados, garantindo que ele esteja no mesmo formato.

Contribuição

Se desejar contribuir para o projeto, faça um fork do repositório, crie um branch com suas alterações e envie um pull request.
Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais informações.
