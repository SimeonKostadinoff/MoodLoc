import json
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
    
with open('data.json', 'w') as outfile:	
	json.dump(alchemy_language.concepts(url='http://www.bbc.co.uk/news/world-us-canada-39394043'), outfile, indent=4)

with open('data.json') as data_file:    
    data = json.load(data_file)

try: 
	for i in range (100):
		concept1 = data["concepts"][i]["text"]
		print(concept1)
except IndexError:
	print("Finished")
	
#Integrate script to db
#Fetch tweets from db and send results back to db