from pyspark.sql import SparkSession

spark = SparkSession.builder \
            .appName("ReaderCsv") \
            .config("spark.jars", "/spark/jars/postgresql-42.7.3.jar") \
            .getOrCreate()

csv_file_path = '/spark/data/data.csv'

df = spark.read.option("multiline",True) \
                .option("encoding", "utf-8")\
                .csv(csv_file_path, 
                    header=True, 
                    sep=',')

print(df.printSchema())
print(df.show(5))