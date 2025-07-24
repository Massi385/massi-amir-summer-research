import requests


model="llama3"


history = " "




while 5 < 6:

    prompt = input()

    history += ( "user: " + prompt + " " )

    prompt = history


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


    history += ( " ai (you): " + data.get("response", "") + " " )


