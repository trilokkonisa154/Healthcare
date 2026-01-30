# ML model training
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("diabetes.csv")

# Select ONLY required features
X = data[[
    "Age",
    "BMI",
    "Glucose",
    "BloodPressure",
    "Outcome"  # temp, will drop later
]]

# Add dummy Gender & FamilyHistory (since dataset doesn’t have them)
data["Gender"] = 0  # assume female = 0
data["FamilyHistory"] = 0  # assume no history

X = data[["Age", "Gender", "BMI", "Glucose", "BloodPressure", "FamilyHistory"]]
y = data["Outcome"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
pickle.dump(model, open("diabetes_model.pkl", "wb"))

print("Model trained with 6 features and saved!")
