# Ponderada 1 

Buenas! Nesta seção, explico o que é e os passos para executar esse projeto. 

## O que é?

O presente projeto nada mais é que uma API com um sistema de gerenciamento de nível de maturidade 2. A camada de visualização é administrada e renderizada pelo Swagger.

## Como executar?

Antes de tudo, é necessário instalar as dependências do projeto. Para isso:

`python -m pip install -r requirements.txt `

Em seguida, inicie o aplicativo para rodar o servidor localmente:
 `python3 app.py`

 Pronto! o projeto está rodando.

Para operar a API, é necessário fazer requisições HTTP. Para isso, utilizaremos o Insomnia. Na pasta static você pode encontrar uma collection pronta com as operações básicas de gerenciamento de tarefas.

Visualização da interface:

Para fazer a autenticação, é necessário selecionar o tipo dela e colocar as credenciais encontradas no código (username: gustavo, password: senha). Neste projeto, usamos o tipo *basic*.

Requisitos das operações:

Para melhor entendimento dos requisitos, visite o Swagger.

**GET** Não é necessário ter um corpo.
**POST** Precisa ter um corpo no formato JSON. É lá que você manipula conforme sua necessidade.
**PUT** Precisa ter um corpo no formato JSON. É lá que você manipula conforme sua necessidade.
**DELETE** Não é necessário ter um corpo.
