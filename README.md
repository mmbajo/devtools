# Dev Tool Mini Demos

This repository is a collection of mini-demos showcasing the usage and capabilities of various development tools in the software engineering landscape. Each folder in this repository contains a self-contained example for a specific tool like Kubernetes, Kafka, RabbitMQ, and many more.

## Table of Contents

- [Getting Started](#getting-started)
- [Tools Covered](#tools-covered)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Docker
- Python 3.x
- Node.js (if applicable)
  
### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/mmbajo/devtools.git
    ```

2. Navigate to the folder of the tool you are interested in:

    ```bash
    cd devtools/Kubernetes
    ```

3. Follow the README in that specific folder to get the demo running.

## Tools Covered

Here's a list of tools for which demos are available:

### [Kubernetes](./Kubernetes/)

A mini-demo showcasing a simple microservices setup using Kubernetes. This demo includes a preprocessing service and an inference service.

### [Kafka](./Kafka/)

This folder contains a Kafka producer and consumer example, focused on real-time messaging. The demo showcases a re-identification task with two cameras.

### [RabbitMQ](./RabbitMQ/)

An example illustrating message queuing using RabbitMQ. A Flask app acts as the producer, while a separate consumer reads the message.

### [Airflow](./Airflow/)

A simple Airflow DAG to showcase data pipeline orchestration. Includes a Spark task example.

### [Spark](./Spark/)

A mini-demo for running Spark tasks both locally and on AWS. Focuses on data processing and manipulation.

### ... (Add more as repository grows)

## Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.