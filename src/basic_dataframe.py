from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkLearning") \
    .getOrCreate()

df = spark.read.csv("data/students.csv", header=True, inferSchema=True)

# df.printSchema()

# df.show()

# df.filter(df.score > 85) \
#     .select("name", "score") \
#     .show()

# df.groupBy("city") \
#     .count() \
#     .show()

result = df.groupBy("city").count()
result.explain("extended")

print("====================================")
result.show()

print("====================================")
print(df.rdd.getNumPartitions())

input("Press Enter to stop Spark...")
spark.stop()