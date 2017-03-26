import json
import views
from watson_developer_cloud import AlchemyLanguageV1

#alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
alchemy_language = AlchemyLanguageV1(api_key='2233ce8c0f1dbea2f9da6e3a2decf0bd7f5eb6ed')
   
with open('data.json', 'w') as outfile:	
	json.dump(alchemy_language.concepts(url="https://en.wikipedia.org/wiki/Association_football"), outfile, indent=4)

with open('data.json') as data_file:    
    data = json.load(data_file)

try: 
	for i in range (100):
		concept = data["concepts"][i]["text"]
		relevance = data["concepts"][i]["relevance"]
		print(concept + " " + relevance)
except IndexError:
	print("Finished")
	
#Integrate script to db
#Fetch tweets from db and send results back to db