import requests
import json

#Define endpoint URL
url = "https://jsonplaceholder.typicode.com/posts"

#Send request
response = requests.get(url)

#Check response
if response.status_code == 200:
    data = json.loads(response.text)

    #Verify Response
    for item in data:
        assert isinstance(item["userId"], int)
        assert isinstance(item["id"], int)
        assert isinstance(item["title"], str)
        assert isinstance(item["body"], str)

    print("Data types verified successfully!")
else:
    print(f"Error: Request failed with status code {response.status_code}")