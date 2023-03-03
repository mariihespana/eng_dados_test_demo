import pandas as pd

# Leitura dos dados em json
data_json = pd.read_json("data.json")

# Transformacao dos dados em dataframe
df = pd.DataFrame(data_json)
# Extraindo o dicionario da lista em cada linha do dataframe
df["ItemList"] = [i[0] for i in data_json.ItemList]
# Transformando o dicionario descritivo dos itens em colunas
df = pd.concat([df.drop(["ItemList"], axis=1), df.ItemList.apply(pd.Series)], axis=1)

# Construção do 2º dataframe (NFeID + Lista de itens associados ao NFEid)
df_itemlist = df[['NFeID','ProductName','Value','Quantity']]

# Excluir coluna de ItemList do primeiro dataframe, que agora poderá buscar a informação através de relacionamento com o 2º dataframe pela chave NFeID
df.drop(columns=["ProductName",'Value','Quantity'], inplace=True)

print("\n Primeiro dataframe: \n ")
print(df)
print("\n Segundo dataframe:  \n" )
print(df_itemlist)