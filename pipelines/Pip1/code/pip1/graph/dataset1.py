from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pip1.config.ConfigStore import *
from pip1.udfs.UDFs import *

def dataset1(spark: SparkSession, in0: DataFrame):
    in0.write.format("json").save("test")
