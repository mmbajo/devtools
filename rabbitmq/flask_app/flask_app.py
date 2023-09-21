from flask import Flask, render_template, request, jsonify
import pika

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        temperature = request.form['temperature']
        humidity = request.form['humidity']

        # Connect to RabbitMQ and send the data
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='temp_humidity')

        message = f"Temperature: {temperature}, Humidity: {humidity}"
        channel.basic_publish(exchange='', routing_key='temp_humidity', body=message)

        connection.close()

        return jsonify({"status": "success", "temperature": temperature, "humidity": humidity})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)