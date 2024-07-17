
import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import *




class TestSparkSession:
    __test__ = False
    def __init__(self):
        self.__session = self.__get_spark_session()

    def __get_spark_session(self):
        spark = SparkSession.builder \
            .appName("TestApp") \
            .getOrCreate()
        return spark

    def stop(self):
        self.__session.stop()

    def __enter__(self) -> SparkSession:
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            self.__session.stop()
        except:
            print(self.__get_spark_session())
        finally:
            print('Session already terminated')
