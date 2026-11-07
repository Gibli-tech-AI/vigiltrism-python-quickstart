import requests

url = "[https://vigiltrism.ai/api/public/v1/scan](https://vigiltrism.ai/api/public/v1/scan)"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

payload = {
    "prompt": "הכנס לכאן את קלט המשתמש לבדיקה"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
