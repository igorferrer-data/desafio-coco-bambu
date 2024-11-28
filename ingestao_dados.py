from pyspark.sql import SparkSession

# Criar sessão Spark
spark = SparkSession.builder.appName("Desafio Coco Bambu").getOrCreate()

# Dados simulados
data = {
    "dim_lojas": [{"store_id": 1, "locRef": "99 CB CB", "nome_loja": "Loja Lago Sul"}],
    "dim_datas": [{"bus_dt": "2024-01-01", "ano": 2024, "mes": 1, "dia": 1, "dia_da_semana": "Segunda-feira"}],
    "dim_itens": [{"menuItemId": 101, "nome_item": "Camarão Internacional", "categoria": "Prato Principal", "preco": 45.50}],
}

# Criar DataFrames e salvar no Data Lake
for table_name, rows in data.items():
    df = spark.createDataFrame(rows)
    df.write.mode("overwrite").json(f"/data_lake/{table_name}.json")
