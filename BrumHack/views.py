from django.shortcuts import render
import tweepy

# Create your views here.

def tweets(request):
    '''Dsiplay all tweets'''

def base_page():
	'''Tokens go here'''
	auth = tweepy.OAuthHandler('s50kOqoGiWSKWWM2ivCz7rcOe', 'N4SAbdjVIHMZWcWT6HPaysyKX9rN5tjKyPoC6IID49NdiDlS4d')
	auth.set_access_token('338335567-3mqDJ2s2Gz0D9wFd52sLTcpD2hfCo27IVMSn8He8', 'SbgR8QCBMVuIXQ7C9XKmbDfgd4cnvwMI9rP3OTyDwo7ZK')

	api = tweepy.API(auth)

	tweetArray = []
	
	for tweet in tweepy.Cursor(api.search, geocode='51.5073,-0.1277,50km').items(20):
			tweet = tweet.text.encode('utf-8', 'ignore')
			#print(tweet)
			tweetArray.append(tweet)
		
	return tweetArray
	
	#return render(request, 'index.html') # render home page

if __name__ == "__main__":
	#request = 1
	base_page()