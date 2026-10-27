
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5, 7, 9, 3, 6, 8],
    "marks": [20, 25, 35, 40, 50, 60, 70, 80, 30, 55, 72, 90, 38, 65, 85]
}

df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

joblib.dump(model, "student_marks_model.pkl")

print("Model saved successfully!")
