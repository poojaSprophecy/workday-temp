from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline1.config.ConfigStore import *
from pipeline1.udfs.UDFs import *
from prophecy.utils import *
from pipeline1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset1 = dataset1(spark)
    df_Filter_1 = Filter_1(spark, df_dataset1)
    dataset1_1(spark, df_Filter_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline1")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline1")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
