from flask import Flask, request, jsonify, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

iris_classes = ["setosa", "versicolor", "virginica"]

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Iris Classifier</title>
</head>
<body>
    <h2>Iris Flower Prediction</h2>
    <form method="post">
        Sepal Length: <input type="number" step="any" name="sepal_length" required><br><br>
        Sepal Width: <input type="number" step="any" name="sepal_width" required><br><br>
        Petal Length: <input type="number" step="any" name="petal_length" required><br><br>
        Petal Width: <input type="number" step="any" name="petal_width" required><br><br>
        <button type="submit">Predict</button>
    </form>

    {% if prediction %}
        <h3>Prediction: {{ prediction }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        features = np.array([
            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"])
        ]).reshape(1, -1)

        pred = model.predict(features)[0]
        prediction = iris_classes[pred]

    return render_template_string(HTML_FORM, prediction=prediction)


@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json

    features = np.array([
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]).reshape(1, -1)

    pred = model.predict(features)[0]

    return jsonify({"prediction": iris_classes[pred]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
