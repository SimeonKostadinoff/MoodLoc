import json
import views
import time
from watson_developer_cloud import AlchemyLanguageV1

# alchemy_language = AlchemyLanguageV1(api_key='114b204a358f29cc5a74ab894dc82ad19d267752')
alchemy_language = AlchemyLanguageV1(api_key='2233ce8c0f1dbea2f9da6e3a2decf0bd7f5eb6ed')
MAX_TOPICS = 8


def getTweetsTopics(radius, coordinates):
    currentRadius = radius * 0.2

    fields = []
    relevanceValue = []

    while currentRadius <= radius:
        tweets = views.base_page(currentRadius, coordinates)
        savedTweets = []

        for tweet in tweets:
            if tweet not in savedTweets:

                tweet = " ".join(filter(lambda x: x[0] != '@', tweet.split()))

                try:
                    with open('data.json', 'w') as outfile:
                        json.dump(alchemy_language.concepts(text=tweet, max_items=10), outfile, indent=2)
                except:
                    print('Exception1')

                try:
                    with open('data.json') as data_file:
                        data = json.load(data_file)
                except:
                    print('Exception2')

                try:
                    for i in range(MAX_TOPICS):
                        concept = data["concepts"][i]["text"]
                        relevance = data["concepts"][i]["relevance"]
                        fields.append(concept)
                        relevanceValue.append(relevance)

                except:
                    print('Exception3')

                currentRadius = currentRadius + (radius * 0.2)
                savedTweets.append(tweet)

        time.sleep(10)

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

    return relevantFields
