import json


with open("mixed_data_3b.json", "r") as f:
    b3 = json.load(f)


with open("mixed_data_ 8b.json", "r") as f:
    b8 = json.load(f)


#with open("mixed_data_11b.json", "r") as f:
    #b11 = json.load(f)



import matplotlib.pyplot as plt
import numpy as np



print( b3[0]['tempurature'])


############
## stats over time


# get avg of all turn 1 sentiment
# and other stats
# then same for each turn
# then see the graph over time

x = 1

sentiments = []
empathies = []
cohs = []



sentiment = []
empathy =[]
coh = []


x = 1
while x < 10:

    x2 = 1
    while x2 < 30:

        sentiments.append(b8[x2][x][0]['compound'])
        empathies.append(  int(b8[x2][x][1])   )
        cohs.append(  int(b8[x2][x][2]) )
        


        




        x2 += 2
    

    print("here")

    sentiment.append(sum(sentiments) / len(sentiments) )
    print(empathies)
    
    empathy.append(sum(empathies) / len(empathies))
    
    coh.append(sum(cohs) / len(cohs))
    print("here")
    
    sentiments = []
    empathies = []
    cohs = []

    

    x+= 1


print(sentiment)




plt.plot(sentiment, color='blue' )
#plt.plot(empathy)
#plt.plot(coh)
plt.ylabel("sentiment Score") 
plt.xlabel(" turns in conversation ")
plt.grid(True)
plt.show()






print("done with time test")
input("enter something to move on to temp test: ")





























#########
## stats over temp



sentiments = []
empathies = []
cohs = []



sentiment = []
empathy =[]
coh = []





temp = 0

while temp < 1:
    x2 = 1
    while x2 < 30:
        
        print(b8[x2-1])
       
        print(b8[0]['tempurature'])
        if b8[x2-1]['tempurature'] == (temp):

            x = 1
            while x < 10:
                
                sentiments.append(b8[x2][x][0]['compound'])
                empathies.append(  int(b8[x2][x][1])   )
                cohs.append(  int(b8[x2][x][2]) )


                x += 1



        x2 += 2


    sentiment.append(sum(sentiments) / len(sentiments) )
    print(empathies)
    
    empathy.append(sum(empathies) / len(empathies))
    
    coh.append(sum(cohs) / len(cohs))
    print("here")
    

    sentiments = []
    empathies = []
    cohs = []

    

    temp += .4


print(sentiment)


#plt.plot(sentiment, color='blue' )
#plt.plot(empathy, color='red' )
#plt.plot(coh, color='green' )
#plt.plot(empathy)
#plt.plot(coh)
plt.ylabel("Empathy Score") 
plt.xlabel(" turns in conversation ")
plt.grid(True)
plt.show()





















##############
## stats over model size














