import json
import views
from watson_developer_cloud import AlchemyLanguageV1

#alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
alchemy_language = AlchemyLanguageV1(api_key='2233ce8c0f1dbea2f9da6e3a2decf0bd7f5eb6ed')

radius = 5    
currentRadius = (radius*0.50)	

fields = []
relevanceValue = []	
tweets = []	
savedTweets = []
	
while(currentRadius <= radius):
	tweets = views.base_page(currentRadius)
		
	for tweet in tweets:
		if tweet not in savedTweets:
			print(tweet)

			try:
				with open('data.json', 'w') as outfile:	
					json.dump(alchemy_language.concepts(text=tweet), outfile, indent=2)
			except:
				print(" ")
				
			try:
				with open('data.json') as data_file:    
					data = json.load(data_file)
			except:
				print(" ")	
					
			try: 
				for i in range (100):
					concept = data["concepts"][i]["text"] 
					relevance = data["concepts"][i]["relevance"]
					
					fields.append(concept)
					relevanceValue.append(relevance)
					
					print(concept + " " + relevance)
			except:
				print(" ")
			
			currentRadius = currentRadius + (radius*0.50)
			savedTweets.append(tweet)

#create two dimensional array			
h = len(fields)		
Matrix = []
	
for index in range(0, h):
	Matrix.append([fields[index], relevanceValue[index]])

#normalisation of data
#for each field, get its relevanceValue along with others for the same field. add field and sum to new array
#mark each subsequent repeated field name with 0

relevantFields = []
i = 1

for index in range(0, h):
	if (Matrix[index][0] != 0):
		sum = float(Matrix[index][1])
	
		for index2 in range(index+1, h):
			if (Matrix[index2][0] == Matrix[index][0]):
				sum += float(Matrix[index2][1])
				#print(sum)
				Matrix[index2][0] = 0
				
		relevantFields.append([Matrix[index][0], sum])
		print(Matrix[index][0] + " " + str(sum))
		i += 1
		
#sort list
for index2 in range(1, (i-1)):
	currentValue = float(relevantFields[index2][1])
	tmpString = relevantFields[index2][0]
	position = index2
	
	while position > 0 and relevantFields[position-1][1] > currentValue:
		relevantFields[position][0] = relevantFields[position-1][0]
		relevantFields[position][1] = relevantFields[position-1][1]
		position = position-1
		
	relevantFields[position][1] = currentValue
	relevantFields[position][0] = tmpString
		
for index3 in range(0, (i-1)):
	print(relevantFields[index3][0] + " " + str(relevantFields[index3][1]))