# Apache Beam Docker Sample

This project demonstrates how to containerize a simple Apache Beam Python pipeline using Docker. The pipeline performs a basic word count operation.

## Prerequisites

- Docker installed on your local machine
- Python 3.7 or higher (for local testing, optional)

## Directory Structure

```plaintext
.
├── Dockerfile
├── README.md
└── sample_beam.py
```

## Instructions

### Building the Docker Image

1. Navigate to the directory containing the `Dockerfile` and `sample_beam.py` in your terminal.
2. Build the Docker image with the following command:

    ```bash
    docker build -t apache-beam-sample .
    ```

### Running the Docker Container

Run the Docker container using the following command:

```bash
docker run apache-beam-sample
```

### Expected Output

Upon running the container, you should see output similar to the following, which indicates the word count operation was executed successfully:

```plaintext
('hello', 1)
('world', 1)
('I', 1)
('am', 1)
('learning', 1)
('apache', 1)
('beam', 1)
('this', 1)
('is', 1)
('a', 1)
('sample', 1)
```

## Additional Notes

This example uses Apache Beam's DirectRunner, suitable for development and testing. For more advanced usage and different runners, refer to the official [Apache Beam documentation](https://beam.apache.org/documentation/runners/capability-matrix/).

# When to Use Apache Spark, Apache Beam, and Apache Airflow

## Apache Spark

### When to use
- When you have large-scale data processing tasks.
- For running machine learning algorithms at scale.
- When you need a general-purpose, in-memory distributed data processing engine.

### Sample Use-case
- Batch processing and real-time analytics on large datasets.

## Apache Beam

### When to use
- When you need a unified model for both batch and stream data processing.
- When you're working with multiple data processing engines.
  
### Sample Use-case
- Real-time data ingestion and transformation that can run on multiple runners like Apache Flink, Google Cloud Dataflow, etc.

## Apache Airflow

### When to use
- When you need to schedule and orchestrate complex workflows.
- For automating the flow of data between systems.

### Sample Use-case
- ETL (Extract, Transform, Load) workflows, data warehousing tasks.


