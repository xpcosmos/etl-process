"""Insert data from file to SQL Database"""
from pyspark.sql import SparkSession

CSV_FILE_PATH = '/spark/data/data.csv'

PSQL_HOST = 'raw-database'
PSQL_PORT = '5432'
PSQL_DB = 'raw'

jdbc_connection = f"jdbc:postgresql://{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB}"

spark = SparkSession.builder \
            .appName("ReaderCsv") \
            .config("spark.jars", "/spark/jars/postgresql-42.7.3.jar") \
            .getOrCreate()

df = spark.read.option("multiline",True) \
                .option("encoding", "utf-8")\
                .csv(CSV_FILE_PATH,
                    header=True)

print(f'\n\n{jdbc_connection}\n\n')
print(df.printSchema())

df.write.format("jdbc").mode("overwrite") \
        .option("url", jdbc_connection) \
        .option("truncate", 'true') \
        .option("driver","org.postgresql.Driver") \
        .option("dbtable","public.animals") \
        .option("user","spark") \
        .option("password", "sparkpassword") \
        .save()
