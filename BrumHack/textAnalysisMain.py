import json
import views
from watson_developer_cloud import AlchemyLanguageV1

#alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
alchemy_language = AlchemyLanguageV1(api_key='2233ce8c0f1dbea2f9da6e3a2decf0bd7f5eb6ed')

radius = 5    
currentRadius = (radius*0.20)	

fields = []
relevanceValue = []	
tweets = []	
	
while(currentRadius <= radius):
	tweets = views.base_page(currentRadius)
		
	for tweet in tweets:
		if tweet not in tweets:
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
			
			currentRadius = currentRadius + (radius*0.20)
			tweets.append(tweet)

#create two dimensional array			
h = len(fields)		
Matrix = []
	
for index in range(0, (h-1)):
	Matrix.append([fields[index], relevanceValue[index]])

#normalisation of data
#for each field, get its relevanceValue along with others for the same field. add field and sum to new array
#mark each subsequent repeated field name with 0

relevantFields = []

for index in range(0, (h-1)):
	if (Matrix[index][0] != 0):
		sum = Matrix[index][1]
	
		for index2 in range(index+1, (h-1)):
			if (Matrix[index2][0] == Matrix[index][0]):
				sum += Matrix[index2][1]
				Matrix[index2][0] = 0
				
		relevantFields.append([Matrix[index][0], sum])
				
#sort list
for index in range(1, (h-1)):
	currentValue = int(Matrix[index][1])
	tmpString = Matrix[index][0]
	position = index
	
	while position > 0 and Matrix[position-1][1] > currentValue:
		Matrix[position][0] = Matrix[position-1][0]
		Matrix[position][1] = Matrix[position-1][1]
		position = position-1
		
	Matrix[position][1] = currentValue
	Matrix[position][0] = tmpString
		
for index in range(0, (h-1)):
	print(Matrix[index][0] + " " + Matrix[index][1])