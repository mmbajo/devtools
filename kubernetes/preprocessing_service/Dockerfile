# preprocessing_service/Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY preprocessing_app.py .

CMD ["python", "preprocessing_app.py"]