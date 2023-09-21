# Kubernetes Demo for Preprocessing and Inference Services

## Overview

This project provides a Kubernetes-based solution to run two separate services for data preprocessing and inference. Both services are containerized using Docker and orchestrated via Kubernetes. This demo is aimed at demonstrating the scalability and manageability of machine learning services in a Kubernetes environment.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Expose Services](#expose-services)
5. [Monitoring](#monitoring)
6. [Contributing](#contributing)
7. [License](#license)

## Prerequisites

- Docker
- Kubernetes (Minikube or a cloud-based cluster)
- kubectl

## Installation

### Clone the Repository

```bash
git clone https://github.com/mmbajo/devtools.git
cd kubernetes
```

### Build Docker Images

Run the following commands to build the Docker images for both services:

For Preprocessing Service:

```bash
docker build -t preprocessing-service:latest ./preprocessing_service
```

For Inference Service:

```bash
docker build -t inference-service:latest ./inference_service
```

### Deploy to Kubernetes

Apply the Kubernetes manifests to deploy both services and their respective deployments:

```bash
kubectl apply -f k8s_manifests/
```

## Usage

Once deployed, you can interact with these services by sending HTTP requests. You can also scale the services up or down using `kubectl`.

## Expose Services

### Using NodePort

```bash
kubectl expose deployment preprocessing-service --type=NodePort --port=8080
kubectl expose deployment inference-service --type=NodePort --port=8081
```

### Using LoadBalancer

If you are using a cloud provider:

```bash
kubectl expose deployment preprocessing-service --type=LoadBalancer --port=8080 --target-port=8080
kubectl expose deployment inference-service --type=LoadBalancer --port=8081 --target-port=8081
```

## Monitoring

The demo doesn't include a monitoring solution, but in a real-world scenario, you could use tools like Prometheus and Grafana.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code contributions.

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.
