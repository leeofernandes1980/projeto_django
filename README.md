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
