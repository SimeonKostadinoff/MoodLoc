from django.shortcuts import render
import tweepy

# Create your views here.

def tweets(request):
        '''Dsiplay all tweets'''


def base_page(request):
        '''Token goes here'''
        auth = tweepy.OAuthHandler('', '')
        auth.set_access_token('', '')

        api = tweepy.API(auth)

        for tweet in tweepy.Cursor(api.search, geocode='51.5073,-0.1277,50km').items(20):
                print(tweet.text)

        return render(request, 'index.html') # render home page
