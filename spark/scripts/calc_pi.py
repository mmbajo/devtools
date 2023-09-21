from pyspark.sql import SparkSession
import random

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Pi Calculation Example") \
        .getOrCreate()
    
    NUM_SAMPLES = 100000000000
    
    # Create an RDD with NUM_SAMPLES entries, then filter it
    count = spark.sparkContext.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
    
    print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))

    spark.stop()