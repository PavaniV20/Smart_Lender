import os
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Epic 4 Mock Models Setup ---
# In production, replace these with: joblib.load('model.pkl')
MODELS = {
    "Decision Tree": {"accuracy": 0.82, "algorithm": "DecisionTreeClassifier"},
    "Random Forest": {"accuracy": 0.87, "algorithm": "RandomForestClassifier"},
    "KNN": {"accuracy": 0.79, "algorithm": "KNeighborsClassifier"},
    "XGBoost": {"accuracy": 0.89, "algorithm": "XGBClassifier"}
}

def preprocess_and_predict(data, model_name):
    """
    Simulates Epic 3 Data Pre-Processing & Epic 4 Model Prediction
    based on the database ERD attributes provided.
    """
    # Extract values matching LOAN_APPLICATION schema
    try:
        income = float(data.get("income", 0))
        coapplicant_income = float(data.get("coapplicant_income", 0))
        loan_amount = float(data.get("loan_amount", 0))
        credit_history_status = int(data.get("credit_history", 1))
    except ValueError:
        return "Rejected", 0.15

    # Simple rule-based mock logic resembling a trained XGBoost/RF tree boundary
    score = 0.0
    if credit_history_status == 1: score += 0.4
    if income + coapplicant_income > (loan_amount / 2): score += 0.3
    if income > 4000: score += 0.2
    
    # Introduce slight random variance depending on model accuracy tier
    accuracy_factor = MODELS.get(model_name, {"accuracy": 0.8})["accuracy"]
    probability = min(max(score * accuracy_factor + random.uniform(-0.05, 0.05), 0.01), 0.99)
    
    status = "Approved" if probability >= 0.5 else "Rejected"
    return status, round(probability, 4)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_response = None
    
    if request.method == "POST":
        # Form Data Collection
        form_data = {
            "gender": request.form.get("gender"),
            "married": request.form.get("married"),
            "education": request.form.get("education"),
            "self_employed": request.form.get("self_employed"),
            "dependents": request.form.get("dependents"),
            "property_area": request.form.get("property_area"),
            "credit_history": request.form.get("credit_history"),
            "income": request.form.get("income"),
            "coapplicant_income": request.form.get("coapplicant_income"),
            "loan_amount": request.form.get("loan_amount"),
            "loan_term": request.form.get("loan_term"),
            "model_choice": request.form.get("model_choice", "XGBoost")
        }
        
        # ML Execution
        status, probability = preprocess_and_predict(form_data, form_data["model_choice"])
        
        # Structuring payload matching the PREDICTION_RESULT table schema
        prediction_response = {
            "prediction_id": random.randint(10000, 99999),
            "loan_id": random.randint(5000, 9999),
            "model_id": random.randint(1, 4),
            "model_used": form_data["model_choice"],
            "prediction_status": status,
            "probability_score": probability,
            "prediction_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    return render_template("index.html", models=MODELS, result=prediction_response)

if __name__ == "__main__":
    # Hugging Face Spaces requires binding to port 7860
    app.run(host="0.0.0.0", port=7860, debug=True)