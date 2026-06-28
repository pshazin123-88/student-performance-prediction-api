from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoders
model = joblib.load("model/student_model.pkl")
encoders = joblib.load("model/encoders.pkl")

@app.route("/")
def home():
    return jsonify({
        "message": "Student Performance Prediction API is Running!"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame([data])

        # Encode categorical columns
        for col in encoders:
            if col in input_df.columns:
                input_df[col] = encoders[col].transform(input_df[col])

        prediction = model.predict(input_df)[0]

        result = "Pass" if prediction == 1 else "Fail"

        return jsonify({
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)