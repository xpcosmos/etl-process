# pylint: disable=unused-wildcard-import, wildcard-import, unused-import, redefined-builtin, broad-exception-caught
"""Test if Spark Session is working appropriately"""
import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import *




class TestSparkSession:
    """Test Spark Session"""
    __test__ = False
    def __init__(self):
        self.__session = self.__get_spark_session()

    def __get_spark_session(self):
        spark = SparkSession.builder \
            .appName("TestApp") \
            .getOrCreate()
        return spark

    def stop(self):
        """Stop Spark Session"""
        self.__session.stop()

    def __enter__(self) -> SparkSession:
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            self.__session.stop()
        except Exception as error:
            print(self.__get_spark_session(), error, sep='\n')
        finally:
            print('Session already terminated')
