import requests
import json

#Define endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

#request payload
payload = {
    "title": "recommendation",
    "body": "motorcycle",
    "userId": 12
}

#Send POST request
response = requests.post(url, json=payload, headers={"Content-Type" : "application/json"} )

print(response.json())

#Check response
if response.status_code == 201:
    response_data = json.loads(response.text)

    for key, value in payload.items():
        assert response_data[key] == value, f"{key} mismatch in response"

    print("Response matches payload successfully!")
else:
    print(f"Error: Request failed with status code {response.status_code}")
