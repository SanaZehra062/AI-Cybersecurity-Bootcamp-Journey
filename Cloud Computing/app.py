# code to interact with a deployed OpenAI model on Azure
import requests
endpoint = "write your end point here"
api_key = "write your api key"
deployment_name = "gpt-4.1" 
url = f"{endpoint}openai/deployments/{deployment_name}/chat/completions?api-version=2023-05-15"
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},

        {"role": "user", "content": "What is cloud computing explain briefly"}

    ]
}
response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])