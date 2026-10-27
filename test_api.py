
import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "study_hours": 5
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Prediction:", response.json())
