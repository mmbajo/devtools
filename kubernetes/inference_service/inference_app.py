from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/infer", methods=["POST"])
def infer():
    data = request.json
    # Your inference code here
    result = {"result": data}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)