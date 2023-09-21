from pyspark.sql import SparkSession

def main():
    # Initialize a Spark session
    spark = SparkSession.builder \
        .appName("Simple Spark Example") \
        .getOrCreate()

    # Read CSV file into a DataFrame
    df = spark.read.csv("data.csv", header=True, inferSchema=True)

    # Show the DataFrame
    print("Initial DataFrame:")
    df.show()

    # Show DataFrame Schema
    print("Schema of DataFrame:")
    df.printSchema()

    # Perform SQL-like queries
    print("People older than 25:")
    df.filter(df.age > 25).show()

    # Group by and count by city
    print("Count of people by city:")
    df.groupBy("city").count().show()

    # Stop the Spark session
    spark.stop()
    

if __name__ == "__main__":
    main()