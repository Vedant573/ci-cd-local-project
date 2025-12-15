from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    return jsonify({"message": "ATS logic here"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


