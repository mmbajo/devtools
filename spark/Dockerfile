# Use a base image with Java and Python
FROM openjdk:11-jre-slim-buster

# Install Python 3
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip

# Set environment variables for Spark and Hadoop versions
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2

# Download and install Apache Spark
RUN apt-get install -y wget && \
    wget https://downloads.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar -xvf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

# Set Spark environment variables
ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Install PySpark
RUN pip3 install pyspark==$SPARK_VERSION

# Create a directory for your work
RUN mkdir /workspace

# Expose ports (4040 for Spark Web UI)
EXPOSE 4040

# Working directory
WORKDIR /workspace

# Default command (run Spark shell)
CMD ["/spark/bin/spark-shell"]