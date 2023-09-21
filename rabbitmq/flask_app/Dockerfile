# Use the Python 3.8 image
FROM python:3.8

# Install required packages
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# Copy the Flask app into the container
COPY ./flask_app.py /app/
COPY ./templates /app/templates/
COPY ./static /app/static/

# Set working directory and expose the necessary port
WORKDIR /app
EXPOSE 5000

# Run the app
CMD ["python", "./flask_app.py"]