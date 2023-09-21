# Use an official Python runtime as a base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install apache-beam

# Run sample_beam.py when the container launches
CMD ["python", "sample_beam.py"]