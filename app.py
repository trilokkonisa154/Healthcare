from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # ---------- COMMON INPUTS ----------
    mode = request.form.get('mode')
    age = int(request.form.get('age', 0))
    gender = request.form.get('gender')
    activity = request.form.get('activity')

    weight = float(request.form.get('weight', 0))
    height = float(request.form.get('height', 0))

    # ---------- BMI CALCULATION ----------
    height_m = height / 100 if height > 0 else 0
    bmi = round(weight / (height_m ** 2), 2) if height_m > 0 else 0

    score = 0

    # ---------- DIABETES MODE ----------
    if mode == "diabetes":
        sugar = float(request.form.get('sugar', 0))
        family_diabetes = request.form.get('family_diabetes')

        if age > 45:
            score += 1
        if sugar > 140:
            score += 2
        if bmi > 25:
            score += 1
        if activity == "inactive":
            score += 1
        if family_diabetes == "yes":
            score += 1

        disease = "🩸 Diabetes"

    # ---------- HEART DISEASE MODE ----------
    elif mode == "heart":
        bp = float(request.form.get('bp', 0))
        cholesterol = float(request.form.get('cholesterol', 0))
        smoking = request.form.get('smoking')
        family_heart = request.form.get('family_heart')

        if age > 45:
            score += 1
        if bp > 130:
            score += 1
        if cholesterol > 200:
            score += 2
        if bmi > 25:
            score += 1
        if activity == "inactive":
            score += 1
        if smoking == "yes":
            score += 1
        if family_heart == "yes":
            score += 1

        disease = "❤️ Heart Disease"

    # ---------- RISK LEVEL ----------
    if score >= 4:
        result = "High Risk"
        level = "high"
    elif score >= 2:
        result = "Moderate Risk"
        level = "moderate"
    else:
        result = "Low Risk"
        level = "low"

    # ---------- HEALTH ADVICE ----------
    if level == "high":
        if mode == "diabetes":
            advice = [
                "Reduce sugar and refined carbohydrate intake",
                "Exercise at least 30 minutes daily",
                "Maintain a healthy BMI",
                "Monitor blood sugar regularly",
                "Consult a doctor for proper diagnosis"
            ]
        else:  # heart
            advice = [
                "Reduce salt and fatty food intake",
                "Quit smoking immediately",
                "Engage in regular cardio exercise",
                "Control blood pressure and cholesterol",
                "Consult a cardiologist for evaluation"
            ]

    elif level == "moderate":
        advice = [
            "Maintain a balanced diet",
            "Increase physical activity",
            "Monitor health parameters regularly",
            "Avoid unhealthy habits"
        ]

    else:  # low risk
        advice = [
            "Continue your healthy lifestyle",
            "Maintain regular exercise",
            "Have periodic health check-ups"
        ]

    # ---------- RENDER RESULT ----------
    return render_template(
        "result.html",
        disease=disease,
        result=result,
        level=level,
        bmi=bmi,
        advice=advice
    )

if __name__ == "__main__":
    app.run()

