# Student Marks Prediction System

## Project Overview
This project predicts estimated student marks based on study hours using Machine Learning.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Flask
- Joblib

## Project Workflow
1. Create and prepare the dataset.
2. Split the data into training and testing sets.
3. Train a Linear Regression model.
4. Evaluate the model using Mean Absolute Error and R² score.
5. Save the trained model using Joblib.
6. Create a Flask API for predictions.
7. Test the API using Python Requests.

## Files
- `train_model.py` — trains and evaluates the model.
- `app.py` — provides the prediction API.
- `test_api.py` — tests the API.
- `student_marks_model.pkl` — saved trained model.

## How to Run
Install dependencies:

```bash
python -m pip install pandas scikit-learn joblib flask requests
```

Train the model:

```bash
python train_model.py
```

Start the API:

```bash
python app.py
```

Test the API in a second terminal:

```bash
python test_api.py
```

## API Input Example
```json
{"study_hours": 5}
```

The API returns an estimated marks prediction. This is a demonstration project using a small sample dataset, so predictions are not suitable for real academic decisions.

## Author
Gaurav Garasiya