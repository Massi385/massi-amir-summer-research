import json


with open("mixed_data_3b.json", "r") as f:
    b3 = json.load(f)


with open("mixed_data_ 8b.json", "r") as f:
    b8 = json.load(f)


#with open("mixed_data_11b.json", "r") as f:
    #b11 = json.load(f)

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
data.append( ['hell'] )


data = [


]



print(b3[1][1][0])


data.append(['    ' ])
data.append(['model 3.2','3b parameter'])


x3 = 1
while x3 < 3:
    data.append(['    ' ])
    x3 += 1









x = 1
while x < 30:

    data.append([ 'tempurature', b3[x-1]['tempurature']  ]     )
    data.append([ 'paremeter', '3 billion' ]     )
    data.append([ 'scenario', b3[x-1]['protocol']  ]     )



    turns = [' ',' ',' ']
    sentiment= [' ',' ','sentiment:']
    empathy= [' ',' ','empathy:']
    coherance = [' ',' ','coherence:']
    

    x2 = 1

    while x2 < 12:

        turns.append("turn" + str(x2))
        sentiment.append(b3[x][x2][0]['compound'])
        empathy.append(b3[x][x2][1])
        coherance.append(b3[x][x2][2])        

        
        x2 += 1


    data.append(turns)
    data.append(sentiment)
    data.append(empathy)
    data.append(coherance)



    x3 = 1
    while x3 < 5:
        data.append(['    ' ])
        x3 += 1
    x += 2


#### 8 b parameter

data.append(['    ' ])
data.append(['model 3','8b parameter'])


x3 = 1
while x3 < 15:
    data.append(['    ' ])
    x3 += 1









x = 1
while x < 30:

    data.append([ 'tempurature', b8[x-1]['tempurature']  ]     )
    data.append([ 'paremeter', '8 billion' ]     )
    data.append([ 'scenario', b8[x-1]['protocol']  ]     )



    turns = [' ',' ',' ']
    sentiment= [' ',' ','sentiment:']
    empathy= [' ',' ','empathy:']
    coherance = [' ',' ','coherence:']
    

    x2 = 1

    while x2 < 12:

        turns.append("turn" + str(x2))
        sentiment.append(b8[x][x2][0]['compound'])
        empathy.append(b8[x][x2][1])
        coherance.append(b8[x][x2][2])        

        
        x2 += 1


    data.append(turns)
    data.append(sentiment)
    data.append(empathy)
    data.append(coherance)



    x3 = 1
    while x3 < 5:
        data.append(['    ' ])
        x3 += 1
    x += 2


###### 11 billion




import csv

# Create CSV file
with open('llmexchangedata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
