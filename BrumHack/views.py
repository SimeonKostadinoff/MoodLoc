from django.shortcuts import render
import tweepy

# Create your views here.

def tweets(request):
    '''Dsiplay all tweets'''

def base_page(radius):
	'''Tokens go here'''
	#auth = tweepy.OAuthHandler('s50kOqoGiWSKWWM2ivCz7rcOe', 'N4SAbdjVIHMZWcWT6HPaysyKX9rN5tjKyPoC6IID49NdiDlS4d')
	#auth.set_access_token('338335567-3mqDJ2s2Gz0D9wFd52sLTcpD2hfCo27IVMSn8He8', 'SbgR8QCBMVuIXQ7C9XKmbDfgd4cnvwMI9rP3OTyDwo7ZK')

	#auth = tweepy.OAuthHandler('jYyyQWZqGXerv4hQ8C0zUhCuf', 'k8a1gjF8iHDwMFn8xkofvTUTt5zjWgMDjmJhCGn3Oxaei7W5aF')
	#auth.set_access_token('845836175738900480-Xoqdks9tLZabTNHzpD9nn43IgsKrC8K', 'AKDly5aaRlcJejNCjrH1mlgQJ62EfmVUxWcYDx9AWVrv9')
		
	auth = tweepy.OAuthHandler('0Dcm8BKuMuAd3smDtxtz7o1L9', 'a5usa3zEs8Qj822oSj7eC7ZaMI65IvIv5AuUlnfrmzMg5lXDzv')
	auth.set_access_token('845861791087366144-jbjnyXaIGhn0lhrMlTM7FavKWnIsCoK', '782TjWmSI65U7RL1PT1ZLZ6oKYDxKVP5Mjx6GDyszEGab')
	
	api = tweepy.API(auth)

	tweetArray = []
	
	for tweet in tweepy.Cursor(api.search, geocode='51.5073,-0.1277,' + str(radius) + "km").items(100):
			tweet = tweet.text.encode('utf-8', 'ignore')
			tweetArray.append(tweet)
	
	#tweetString = ' '.join(tweetArray)
		
	return tweetArray
	#return tweetString
	
	#return render(request, 'index.html') # render home page

if __name__ == "__main__":
	#request = 1
	base_page(5)