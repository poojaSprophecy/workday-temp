from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *

def dataset1(spark: SparkSession) -> DataFrame:
    return spark.read.format("json").schema(StructType([StructField("etst", StringType(), True)])).load("test")
