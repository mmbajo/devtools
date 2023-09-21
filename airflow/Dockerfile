# Use the official Airflow image as the base image
FROM apache/airflow:2.1.2

# Environment variables
ENV AIRFLOW_HOME=/usr/local/airflow
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////usr/local/airflow/airflow.db
ENV AIRFLOW__CORE__LOAD_EXAMPLES=false

# Install additional dependencies and packages
USER root
RUN apt-get update -y && \
    apt-get install -y \
    vim \
    curl \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Switch to Airflow user and setup Airflow with "db init"
USER airflow
RUN airflow db init

# Copy DAGs into the image (Optional)
# COPY dags/ ${AIRFLOW_HOME}/dags/

# Expose web server and worker ports
EXPOSE 8080 8793

# Run Airflow webserver and scheduler on container startup
CMD ["airflow", "scheduler", "&", "airflow", "webserver"]