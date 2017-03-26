from django.shortcuts import render
import tweepy


# Create your views here.

def tweets(request):
    '''Dsiplay all tweets'''


def base_page(radius, coordinates):
    '''Tokens go here'''
    auth = tweepy.OAuthHandler('jYyyQWZqGXerv4hQ8C0zUhCuf', 'k8a1gjF8iHDwMFn8xkofvTUTt5zjWgMDjmJhCGn3Oxaei7W5aF')
    auth.set_access_token('845836175738900480-Xoqdks9tLZabTNHzpD9nn43IgsKrC8K',
                          'AKDly5aaRlcJejNCjrH1mlgQJ62EfmVUxWcYDx9AWVrv9')

    api = tweepy.API(auth)

    tweetArray = []
    all_tweets = tweepy.Cursor(api.search, geocode=coordinates + ',' + str(radius) + "km").items(1000)
    for tweet in all_tweets:
        tweet = tweet.text.encode('utf-8', 'ignore')
        tweetArray.append(tweet)

    # tweetString = ' '.join(tweetArray)

    return tweetArray


# return tweetString

# return render(request, 'index.html') # render home page

if __name__ == "__main__":
    # request = 1
    base_page(5)
