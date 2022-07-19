1. Pré-requisitos:
* Python 3.8.8
* Poetry

2. Rodando a aplicação.
* para conferir se a conexão com o banco está ok,você pode instalar o dbeaver para visualização e manipulação do banco de dados.
* Dentro do dbeaver você deve criar uma nova conexão POSTGRES com o nome dbMinhaEstante que é o nome da base de dados. O usuario é postgres e a senha também.
*  caso de um erro de conexão refusa, basta dar um sudo service postgresql restart que resolve. ( Não deve ocorrer esse erro ).

* Na aplicação, acesse a pasta minha estante, entre na env com o poetry shell. após isso você deve rodar a aplicação com: uvicorn main:app --reload --host 0.0.0.0.
