# Imports
import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Conexão com o bd
dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-9R7CQ7Q;"
                 "Database=ContosoRetailDW;"
                 )

conexao = pyodbc.connect(dados_conexao)
print('A conexão com o banco de dados foi bem sucedida!')

# Cursor do pyodbc
# cursor = conexao.cursor() #Não é necessário nesse caso

# Iniciando o desafio com o uso do pandas
df = pd.read_sql(
    'SELECT DateKey, SalesAmount, TotalCost, DiscountAmount FROM ContosoRetailDW.dbo.FactSales', conexao)
print(df)

df["Lucro"] = df["SalesAmount"] - (df["TotalCost"] + df["DiscountAmount"])

new_df = df.groupby(["DateKey"]).sum()
print(df["Lucro"])

grafico = new_df["Lucro"].plot(figsize=(15, 5))
grafico.yaxis.set_major_formatter(
    matplotlib.ticker.StrMethodFormatter('${x:,.0f}'))
plt.show()
