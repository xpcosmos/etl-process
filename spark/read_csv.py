from pyspark.sql import SparkSession

spark = SparkSession.builder \
            .appName("ReaderCsv") \
            .getOrCreate()

csv_file_path = 'spark/data/data.csv'

df = spark.read.option("multiline",True) \
                .option("encoding", "utf-8")\
                .csv(csv_file_path, 
                    header=True, 
                    sep=',')

print(df.printSchema())
print(df.show(5))


# Saving data to a JDBC source
df.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:dbserver") \
    .option("dbtable", "schema.tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .save()