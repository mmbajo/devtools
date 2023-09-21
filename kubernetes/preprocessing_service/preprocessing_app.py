from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/preprocess", methods=["POST"])
def preprocess():
    data = request.json
    # Your preprocessing code here
    processed_data = {"processed": data}
    return jsonify(processed_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)