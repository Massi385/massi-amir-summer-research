
import requests


model="llama3"

prompt = input()


response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    
data = response.json()
    

print(data.get("response", ""))









