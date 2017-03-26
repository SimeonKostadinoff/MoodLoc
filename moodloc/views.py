from django.shortcuts import render
import tweepy
import json, requests

# Create your views here.

def tweets(request, location):
        #Tokens go here
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyC8ljIetSrO_QgEa-wJDqLHaIbEB0PRJ2U"
        auth = tweepy.OAuthHandler('s50kOqoGiWSKWWM2ivCz7rcOe', 'N4SAbdjVIHMZWcWT6HPaysyKX9rN5tjKyPoC6IID49NdiDlS4d')
        auth.set_access_token('338335567-3mqDJ2s2Gz0D9wFd52sLTcpD2hfCo27IVMSn8He8',
                              'SbgR8QCBMVuIXQ7C9XKmbDfgd4cnvwMI9rP3OTyDwo7ZK')

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
