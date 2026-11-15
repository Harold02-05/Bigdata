Big Data - Fase 3
Descripción:
Proyecto desarrollado para la Fase 3 del curso Big Data de la UNAD utilizando Apache Spark, PySpark y Apache Kafka.

La solución implementa procesos de limpieza, transformación, análisis exploratorio y visualización de datos mediante procesamiento batch, además de un escenario de procesamiento de datos en tiempo real utilizando Kafka y Spark Structured Streaming.

Archivos del proyecto
limpieza.py: limpieza y preparación de los datos.
transformacion.py: transformación de datos utilizando Spark.
eda1.py: análisis exploratorio de datos.
visualizacion.py: generación de visualizaciones.
visualizacion2.py: visualizaciones complementarias.
kafka_producer.py: simulación de envío de datos en tiempo real mediante Kafka.
spark_streaming_consumer.py: procesamiento y análisis de datos en streaming con Spark Structured Streaming.
Tecnologías utilizadas
Python
Apache Spark
PySpark
Apache Kafka
Ubuntu Server
Visual Studio Code
Ejecución del procesamiento batch
Ejecutar los scripts en el siguiente orden:

python3 limpieza.py
python3 transformacion.py
python3 eda1.py
python3 visualizacion.py
python3 visualizacion2.py
Ejecución del procesamiento en streaming
Iniciar los servicios de Apache Kafka.
Ejecutar el consumidor Spark:
spark-submit spark_streaming_consumer.py
En una segunda terminal ejecutar el productor:
python3 kafka_producer.py
Los datos serán enviados al tópico Kafka sensor_data y procesados en tiempo real mediante Spark Structured Streaming.

Autor
Harold Hernandez
