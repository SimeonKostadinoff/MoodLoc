import json
import views
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
    
tweets = views.base_page()
	
for tweet in tweets:
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
			concept1 = data["concepts"][i]["text"]
			print(concept1)
	except:
		print(" ")