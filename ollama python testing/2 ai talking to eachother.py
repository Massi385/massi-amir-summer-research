import requests


model="llama3"



# ai 1 is the comedian
# ai 2 is the philosipher

# im adding my own sentence for ai 1 to tell even though i am actualy saying it, both the ais will think ai 2 said it in the beginning of the conversation
# this is just so the conversation can start cause the ai needs something to respond to




# beginning prompts 

history1 = " [ act as if you are a comedian ][ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "


history2 = " [ act as if you are a philosipher ][ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "






################ start of conversation #########

#### ai 1 first message
conversationstarter = "what is your favorite food?"



print(" ai 1: \n" + conversationstarter + " \n\n")


history1 += ( " [ai (you)]:" + conversationstarter + " " )
history2 += ( " [user]: " + conversationstarter + " " )



### ai 2 first message
response = requests.post(
            "http://localhost:11434/api/generate",
            json={                     ########   this entire chunk of code is what actualy talks to the Ollama ai on my computer 
                "model": model,     # this just uses the Ollama model 3, it was defined earlier in the code
                "prompt": history1,  # this is what the ai is actualy told and what it is responding to
                "stream": False  # i dont know what this means yet
            }
        )
data = response.json()





print(" ai 2: \n" + data.get("response", "") + " \n\n")

                
history1 += ( " [user]: " + data.get("response", "") + " " )
history2 += ( " [ai (you)]: " + data.get("response", "") + " " )







################# conversation loop #############

x = 0
while x < 3:


    
    ### ai 1 says something responding to what ai 2 last said ####
    response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": history1,
                "stream": False
            }
        )

    data = response.json()
    print(" ai 1: \n" + data.get("response", "") + " \n\n")

    

    
    history1 += ( " [ai (you)]:" + data.get("response", "") + " " )
    history2 += ( " [user]: " + data.get("response", "") + " " )






    ### ai 2 says something responding to what ai 1 last said ####
    response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": history2,
                "stream": False
            }
        )

    data = response.json()
    print(" ai 2: \n" + data.get("response", "") + " \n\n")
    


    history1 += ( " [user]:" + data.get("response", "") + " " )
    history2 += ( " [ai (you)]: " + data.get("response", "") + " " )





    x += 1








   






























    


