from pyspark.sql import SparkSession

# Создаем SparkSession
spark = SparkSession.builder.appName("Read CSV").getOrCreate()

# Путь к файлу внутри контейнера Spark
file_path = "file:///opt/bitnami/spark/files/cars.csv"

# Читаем CSV файл с использованием Spark
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Выводим первые 10 строк для проверки
df.show(10)
