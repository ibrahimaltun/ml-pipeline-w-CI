import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load("model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    x = [[data["x"]]]
    y_pred = model.predict(x)
    return jsonify({"prediction": y_pred[0]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
