from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *

def dataset1_1(spark: SparkSession, in0: DataFrame):
    in0.write.format("json").save("test")
