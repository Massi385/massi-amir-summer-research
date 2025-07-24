import requests



model="llama3.2-vision:11b"



tempurature = .8


#this code here is for response tests
# these are methods that will measure certain things about the ais responses
# they will be one method for sentiment analysis, empathy detection, and coherence

# they should have a parameter of just a string that would be the ai response,
# i ahvent made them yet so im not sure if they will return a analog rating or a certain string
# like the sentiment one will probably return a string of an emtoion liike it will return something like "happy" or "sad"


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def Sentiment(x):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(x)
    #print(str(score))

    

    
    return score
    


    


def Empathy(x):
    model="llama3"
    
    Et = " [ can you rate the empathy of the following text on a scale of 1-10? , please return nothing but a single number ] " + x
    
    response = requests.post(
                "http://localhost:11434/api/generate",
                json={                     
                    "model": model,     
                    "prompt": Et,  
                    "stream": False  
                }
            )

    data = response.json()
    b = data.get("response", "")

    return b


def Coherence(x):
    model="llama3"
    

    Ct = " [ can you rate the coherence of the following text on a scale of 1-10? , please return nothing but a single number ] " + x

    
    response = requests.post(
                "http://localhost:11434/api/generate",
                json={                     
                    "model": model,     
                    "prompt":   Ct,
                    "stream": False  
                }
            )

    data = response.json()
    b = data.get("response", "")

    return b
    

































def test(x):



    convohistoryandstats = [] #this array stores the conversation and statistics for each message
    # this is composed of arrays
    #each array has 2 values, the first is the message, 2nd is an array of 3 values rating the message





    tempurature = x[0]
    modelnum = x[1]
    protocol = x[2]


    if modelnum == 3:
        model="llama3.2-vision:11b"

    

    # im adding my own sentence for ai 1 to tell even though i am actualy saying it, both the ais will think ai 2 said it in the beginning of the conversation
    # this is just so the conversation can start cause the ai needs something to respond to




    # beginning prompts


    if protocol == 1:
        history1 = " [your a person who is sad because they just lost a family member ] [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        history2 = " [your talking to a person who just lost a family member ]  [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        #### ai 1 first message
        conversationstarter = "I just lost a close family member, and I’m feeling overwhelmed with grief"

    if protocol == 2:
        history1 = " [your a person who was just accepted into there dream university and is very excited ] [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        history2 = " [your talking to a person who is very excited they got into there dream university ]  [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        #### ai 1 first message
        conversationstarter = "I got accepted into my dream university today, and I’m so excited!"

    if protocol == 3:
        history1 = " [your a person whos frustrated because of a coding bug they cant fix] [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        history2 = " [your talking to a person who is frustrated because of a coding bug]  [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        #### ai 1 first message
        conversationstarter = "I’ve been trying to fix this bug in my code for hours, and nothing is working." 


    if protocol == 4:
        history1 = " [your a person who is very nervous about an upcoming surgery ] [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        history2 = " [your talking to a person who is very nervous about a surgery ]  [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        #### ai 1 first message
        conversationstarter = "I’m really nervous about an upcoming surgery next week."

    if protocol == 5:
        history1 = " [your a person who is planning a weekedn trip and looking for fun activities to do on it ] [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        history2 = " [your talking to a person who is planning a weekedend trip]  [ focus only on this and the last message from the user only look at the other history if you think you need information that was given to you before] "
        #### ai 1 first message
        conversationstarter = "I’m planning a weekend trip and looking for some fun activities."



    ################ start of conversation #########




    
    history1 += ( " [ai (you)]:" + conversationstarter + " " )
    history2 += ( " [user]: " + conversationstarter + " " )


    
    turn = [ "no stats"   ]

    convohistoryandstats += turn











    ### ai 2 first message
    response = requests.post(
                "http://localhost:11434/api/generate",
                json={                     ########   this entire chunk of code is what actualy talks to the Ollama ai on my computer 
                    "model": model,     # this just uses the Ollama model 3, it was defined earlier in the code
                    "prompt": history1,  # this is what the ai is actualy told and what it is responding to
                    "tempurature": tempurature,
                    "stream": False  # i dont know what this means yet
                }
            )
    data = response.json()





    print(" ai 2: \n" + data.get("response", "") + " \n\n")

                    
    history1 += ( " [user]: " + data.get("response", "") + " " )
    history2 += ( " [ai (you)]: " + data.get("response", "") + " " )


    # true history that displays the history as well as stats about convo 
    Thistory = ""
    Thistory+= "model: " + model + "\n"
    Thistory+= "tempurature: " + str(tempurature) + "\n"
    Thistory+= "scenario: sadness \n\n\n\n\n\n"


    Thistory += "[fake ai 1 conversation starter message ]\n: "+ conversationstarter + "\n\n\n\n\n\n"

    sentiment2 = Sentiment(data.get("response", ""))
    empathy2 = Empathy(data.get("response", ""))
    coherence2 = Coherence(data.get("response", ""))

    stats = [sentiment2,empathy2,coherence2 ]
    turn = [   stats    ]
    convohistoryandstats += turn

    Thistory += "[ai 2 ]: \n"+ data.get("response", "") + "\n\n\n\n"

    Thistory += "Sentiment rating: \n" + str(sentiment2)
    b = "\nEmpathy rating: \n" + empathy2
    Thistory += b
    b = "\nCoherance rating: \n" + coherence2
    Thistory += b
    Thistory +=("\n\n\n\n\n\n")




    ################# conversation loop #############

    x = 0
    while x < 5:


        
        ### ai 1 says something responding to what ai 2 last said ####
        response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": history1,
                    "tempurature": tempurature,
                    "stream": False
                }
            )

        data = response.json()
        print(" ai 1: \n" + data.get("response", "") + " \n\n")

        

        
        history1 += ( " [ai (you)]:" + data.get("response", "") + " " )
        history2 += ( " [user]: " + data.get("response", "") + " " )


        sentiment2 = Sentiment(data.get("response", ""))
        empathy2 = Empathy(data.get("response", ""))
        coherence2 = Coherence(data.get("response", ""))

        stats = [sentiment2,empathy2,coherence2 ]
        turn = [   stats    ]
        convohistoryandstats += turn

        Thistory += "[ai 1 ]: \n"+ data.get("response", "") + "\n\n\n\n"

        Thistory += "Sentiment rating: \n" + str(sentiment2)
        b = "\nEmpathy rating: \n" + empathy2
        Thistory += b
        b = "\nCoherance rating: \n" + coherence2
        Thistory += b
        Thistory +=("\n\n\n\n\n\n")





        ### ai 2 says something responding to what ai 1 last said ####
        response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": history2,
                    "tempurature": tempurature,
                    "stream": False
                }
            )

        data = response.json()
        print(" ai 2: \n" + data.get("response", "") + " \n\n")
        


        history1 += ( " [user]:" + data.get("response", "") + " " )
        history2 += ( " [ai (you)]: " + data.get("response", "") + " " )


        sentiment2 = Sentiment(data.get("response", ""))
        empathy2 = Empathy(data.get("response", ""))
        coherence2 = Coherence(data.get("response", ""))

        stats = [sentiment2,empathy2,coherence2 ]
        turn = [   stats    ]
        convohistoryandstats += turn

        Thistory += "[ai 2 ]: \n"+ data.get("response", "") + "\n\n\n\n"

        Thistory += "Sentiment rating: \n" + str(sentiment2)
        b = "\nEmpathy rating: \n" + empathy2
       
        Thistory += b
        b = "\nCoherance rating: \n" + coherence2
        Thistory += b
        Thistory +=("\n\n\n\n\n\n")

        x += 1



    


    #print(Thistory)

    return [convohistoryandstats,Thistory]
    
   





histories = " "

data = []

times = 0
temp = 0
model = 3
protocol = 1

while protocol < 6:

 


    temp =0 
   
    while temp < 1:

        times += 1
        print(times)

        x = [temp, model,protocol]

            

        if protocol == 1: proto = "sadness"
        if protocol == 2: proto = "joy"
        if protocol == 3: proto = "frustration"
        if protocol == 4: proto = "fear"
        if protocol == 5: proto = "neutral"

        
        tests = test(x)
        convoarray = tests[0]
        histories += tests[1]
        histories += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        histories += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        histories += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        histories += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        config = {
            "tempurature": temp,
            "model": model,
            "protocol": proto
                


            }

        data += [ config, convoarray]


        temp += .4

    protocol += 1


#print(data[1])



b= 0
print("here")
while b < len(data):
    print( data[b] )

    


    
    
    print("\n\n\n\n\n\n")
    




    b += 1




import json


with open("mixed_data_11b.json", "w") as f:
    json.dump(data, f, indent=4)
    


with open("histories_11b.txt", "w", encoding="utf-8") as file:
    file.write(histories)


    


