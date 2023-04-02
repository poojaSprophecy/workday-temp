from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pip1.config.ConfigStore import *
from pip1.udfs.UDFs import *

def test1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("test", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("test")
