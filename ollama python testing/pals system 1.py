# maybe in the future i could ask the ai if the answer given is maybe half correct
# i guess if the user gave a half correct answer the level would stay the same




import requests


model="llama3"


history = " "


topic = "b2 bombers"





x = 0

level = 5


while x < 2:

    if level < 1:
        level = 1

    if level > 10:
        level = 10

    
    prompt = " come up with a question on the topic of " + topic + " "
    prompt = prompt + "that is on a scale of 1-10 a difficulty of " + str(level)
    prompt = prompt + ", return only the question itself and literaly nothing else "



    ## at comes up with question at apropriate level 
    response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

    data = response.json() 
    question = data.get("response", "")

    
    print(question)


    # user answers the question
    answer = input()




    # program asks ai if the answer is correct


    prompt = " is this answer [ " + answer
    prompt = prompt + " ] a correct answer to the question [ " + question
    prompt = prompt + ", if it is correct, reply only with [yes], if its wrong reply only with [no] "


    response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )



    data = response.json() 

    score = data.get("response", "")

    print(score)

    if score == "[yes]" or score == "[YES]"  or score == "[Yes]":
        level += 1

    if score == "[no]" or score == "[NO]"  or score == "[No]":
        level -= 1
    
    














    x += 1





print("\n level: " + str(level))
