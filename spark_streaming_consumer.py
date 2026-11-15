# creo archivo ejecutable para el entorno ubunu con nombre spark_streaming_consumer.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

schema = StructType([
    StructField("sensor_id", IntegerType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("timestamp", StringType(), True)
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)")

parsed_df = json_df.select(
    from_json(col("value"), schema).alias("data")
).select("data.*")

result = parsed_df.groupBy("sensor_id") \
    .agg(
        avg("temperature").alias("temp_promedio"),
        avg("humidity").alias("hum_promedio")
    )

query = result.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()