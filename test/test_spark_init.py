
from test.support_spark.test_start_spark_session import TestSparkSession
from utils.test_time_to_execute import time_measure
from pyspark.sql import SparkSession
from pyspark.sql.functions import *



@time_measure
def test_spark_session_init():
    spark = TestSparkSession()
    spark.stop()
    assert spark != None
