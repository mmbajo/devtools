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

