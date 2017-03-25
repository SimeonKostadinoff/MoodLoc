from django.shortcuts import render
import tweepy
import json, requests

# Create your views here.

def tweets(request, location):
        #Tokens go here

        resp = requests.get(url=url)
        print(resp.content)
        data = resp.json()

        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        loc = repr(lat) + ',' + repr(lng) + ',50km'

        api = tweepy.API(auth)

        for tweet in tweepy.Cursor(api.search, geocode=loc).items(20):
                print(tweet.text.replace("@", ""))

        return render(request, 'index.html')  # render home page


def base_page(request):
        return render(request, 'index.html') # render home page
