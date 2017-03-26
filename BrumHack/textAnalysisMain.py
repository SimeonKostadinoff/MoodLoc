import json
import views
import time
from watson_developer_cloud import AlchemyLanguageV1

# alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
alchemy_language = AlchemyLanguageV1(api_key='352c0a78499fd6c32cb03621b596818ee969b797')
MAX_TOPICS = 8


def getTweetsTopics(radius, coordinates):
    currentRadius = radius

    fields = []
    relevanceValue = []

    #while currentRadius <= radius:
    tweets = views.base_page(currentRadius, coordinates)
    #tweets = ['hello world', 'brum hack', 'api sucks']
    savedTweets = []

    #print(tweets)
    for tweet in tweets:
        if tweet not in savedTweets:

            tweet = " ".join([x if '@' not in x else '' for x in tweet.split()])
            data = {}
            #print(tweet)
            try:
                with open('data.json', 'w') as outfile:
                    json.dump(alchemy_language.concepts(text=tweet, max_items=10), outfile, indent=2)
            except:
                #raise
                pass

            try:
                with open('data.json') as data_file:
                    data = json.load(data_file)
            except:
                #raise
                pass

            try:
                for i in range(MAX_TOPICS):
                    concept = data["concepts"][i]["text"]
                    relevance = data["concepts"][i]["relevance"]
                    fields.append(concept)
                    #print(fields)
                    relevanceValue.append(relevance)

            except:
                #raise
                pass

            savedTweets.append(tweet)

        #currentRadius = currentRadius + (radius * 0.2)
        time.sleep(1)

    # create two dimensional array
    h = len(fields)
    Matrix = []

    for index in range(0, h):
        Matrix.append([fields[index], relevanceValue[index]])

    # normalisation of data
    # for each field, get its relevanceValue along with others for the same field. add field and sum to new array
    # mark each subsequent repeated field name with 0

    relevantFields = []

    for index in range(0, h):
        if (Matrix[index][0] != 0):
            sum = Matrix[index][1]

            for index2 in range(index + 1, h):
                if (Matrix[index2][0] == Matrix[index][0]):
                    sum += Matrix[index2][1]
                    Matrix[index2][0] = 0

            relevantFields.append([Matrix[index][0], sum])
    #print(relevantFields)

    return relevantFields
