"""Test RDD & Parallelize"""
from test.support_spark.test_start_spark_session import TestSparkSession
from utils.test_time_to_execute import time_measure
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


@time_measure
def test_rdd_and_parallelize():
    with TestSparkSession() as ss:
        rdd = ss.sparkContext.parallelize(range(1, 100))  
        sum_result = rdd.sum()
        print(f"Sum is equals to: {sum_result}")
        assert sum_result == 4950