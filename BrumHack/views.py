from django.http import JsonResponse
import tweepy
from classifier import final_classify


# Create your views here.

def tweets(request):
    '''Dsiplay all tweets'''
    pass

def main(request):
    sentence = request.GET.get('sentence')  # get the 'org_id' passed as get request
    result = ''
    if sentence:
        result = final_classify(sentence)

    return JsonResponse({'result': result})


def base_page(radius, coordinates):
    '''Tokens go here'''
    #auth = tweepy.OAuthHandler('jYyyQWZqGXerv4hQ8C0zUhCuf', 'k8a1gjF8iHDwMFn8xkofvTUTt5zjWgMDjmJhCGn3Oxaei7W5aF')
    #auth.set_access_token('845836175738900480-Xoqdks9tLZabTNHzpD9nn43IgsKrC8K', 'AKDly5aaRlcJejNCjrH1mlgQJ62EfmVUxWcYDx9AWVrv9')

    auth = tweepy.OAuthHandler('0Dcm8BKuMuAd3smDtxtz7o1L9', 'a5usa3zEs8Qj822oSj7eC7ZaMI65IvIv5AuUlnfrmzMg5lXDzv')
    auth.set_access_token('845861791087366144-jbjnyXaIGhn0lhrMlTM7FavKWnIsCoK', '782TjWmSI65U7RL1PT1ZLZ6oKYDxKVP5Mjx6GDyszEGab')

    #auth = tweepy.OAuthHandler('s50kOqoGiWSKWWM2ivCz7rcOe', 'N4SAbdjVIHMZWcWT6HPaysyKX9rN5tjKyPoC6IID49NdiDlS4d')
    #auth.set_access_token('338335567-3mqDJ2s2Gz0D9wFd52sLTcpD2hfCo27IVMSn8He8', 'SbgR8QCBMVuIXQ7C9XKmbDfgd4cnvwMI9rP3OTyDwo7ZK')

    #auth = tweepy.OAuthHandler('h2xXZnEsCeT5ZCF3x8Un27g0f', 'WXCUiXhVVbCmVIANQkHMv8MsygQ8V2qeDIZeIUH7aw06zdfOBJ')
    #auth.set_access_token('845933270743310336-EtLq4RCdtkgg6ayfkv3p8IsAEGRxs35', 'MfJdb1cxg8BsOlhWgG5o5qdMCnvDlYNn4e6ocSytwbiLa')

    api = tweepy.API(auth)

    tweetArray = []
    all_tweets = tweepy.Cursor(api.search, geocode=coordinates + ',' + str(radius) + "km").items(100)
    for tweet in all_tweets:
        tweet = tweet.text.encode('utf-8', 'ignore')
        tweet = tweet.decode('utf-8')
        tweetArray.append(tweet)

    # tweetString = ' '.join(tweetArray)

    return tweetArray


# return tweetString

# return render(request, 'index.html') # render home page

