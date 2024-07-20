from pyspark.sql import SparkSession

spark = SparkSession.builder \
            .appName("ReaderCsv") \
            .getOrCreate()

csv_file_path = '/spark/data/data.csv'

df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

print(df.printSchema())
print(df.show(5))
