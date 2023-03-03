from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, round
import pandas as pd

# Criando uma sessão
my_spark = SparkSession.builder.getOrCreate()

transacoes = [{'transacao_id':1, 'total_bruto':3000, 'desconto_percentual':6.99},
              {'transacao_id':2, 'total_bruto':57989, 'desconto_percentual':1.45},
              {'transacao_id':4, 'total_bruto':1, 'desconto_percentual':None},
              {'transacao_id':5, 'total_bruto':34, 'desconto_percentual':0.0}]

# Criando uma tabela spark
data_spark = my_spark.createDataFrame(transacoes)

# Substituindo valor nulo por 0.0 na coluna desconto_percentual
data_spark = data_spark.na.fill(value=0.0, subset=["desconto_percentual"])

# Calculando o valor total com o desconto aplicado
data_spark = data_spark.withColumn("valor_liquido", data_spark.total_bruto * (1-data_spark.desconto_percentual/100))

# Calculando o total líquido da empresa
data_spark.select(round(sum('valor_liquido'),2).alias("valor_liquido_total")).show()