# Week 4: AI Project Deployment & Capstone

## Project Title
Student Marks Prediction System

## 1. Objective
The objective of this project is to develop a Machine Learning application that predicts estimated student marks based on study hours.

## 2. Technologies Used
Python, Pandas, Scikit-learn, Linear Regression, Flask, Joblib and Requests.

## 3. Methodology
A sample dataset containing study hours and marks was created. The dataset was divided into training and testing sets. A Linear Regression model was trained on the training data and evaluated on the test data using Mean Absolute Error and R² score.

## 4. Model Serialization
The trained model was saved in a `.pkl` file using Joblib so it can be loaded later without retraining.

## 5. API Development
A Flask API was developed with a `/predict` endpoint. It accepts study hours as JSON input and returns predicted marks as JSON output.

## 6. Testing
The API was tested using Python Requests. The response status code and prediction output were checked.

## 7. Conclusion
This project demonstrates a basic end-to-end Machine Learning workflow, including data preparation, model training, evaluation, model serialization and API development.

## 8. Limitations
The model uses a small sample dataset and is intended for learning and demonstration only. The Flask API runs locally; online hosting is a separate deployment step.

## 9. Future Scope
The project can be improved with a larger real dataset, a user-friendly interface, additional model evaluation and online hosting.

## GitHub Repository
Add the GitHub repository URL here after uploading the project.