FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY inference_app.py .

CMD ["python", "inference_app.py"]