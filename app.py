
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("student_marks_model.pkl")

@app.route("/")
def home():
    return "Student Marks Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "study_hours" not in data:
            return jsonify({"error": "Please provide study_hours"}), 400

        study_hours = float(data["study_hours"])

        if not 0 <= study_hours <= 24:
            return jsonify({"error": "Study hours must be between 0 and 24"}), 400

        prediction = model.predict([[study_hours]])[0]

        return jsonify({
            "study_hours": study_hours,
            "predicted_marks": round(float(prediction), 2)
        })

    except (TypeError, ValueError):
        return jsonify({"error": "study_hours must be a number"}), 400

if __name__ == "__main__":
    app.run(debug=True)
