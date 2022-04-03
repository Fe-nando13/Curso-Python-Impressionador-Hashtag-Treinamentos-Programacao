import pyodbc

dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-9R7CQ7Q;"
                 "Database=ContosoRetailDW;"
                 )

conexao = pyodbc.connect(dados_conexao)
print('A conexão com o banco de dados foi bem sucedida!')
