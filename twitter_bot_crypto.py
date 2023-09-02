import tweepy
import requests
import time

consumer_key = 'YOUR TWITTER API KEY'
consumer_secret = 'YOUR TWITTER API SECRET KEY'
access_token = 'YOUR TWITTER ACCESS KEY'
access_token_secret = 'YOUR TWITTER ACCESS SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_crypto_assets():
    url = "<REPLACE URL FROM RAPID API OPENSEA URL>"
    
    querystring = {
        "collection_slug": "cryptopunks",
        "order_direction": "desc",
        "limit": "20",
        "include_orders": "false"
    }
    
    headers = {
        "X-RapidAPI-Key": "<REPLACE YOUR API KEY From Rapid API OpenSea>",
        "X-RapidAPI-Host": "opensea13.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"API request failed with status code {response.status_code}.")
        return None

# Function to tweet crypto assets
def tweet_crypto_assets():
    crypto_assets = get_crypto_assets()
    if crypto_assets:
        for asset in crypto_assets["assets"]:
            name = asset["name"]
            image_url = asset["image_url"]
            permalink = asset["permalink"]
            
            tweet = f"📢 New Crypto Asset 📢\n\nName: {name}\n\nImage: {image_url}\n\nPermalink: {permalink}"
            api.update_status(tweet)
            time.sleep(60)  # Tweet every 60 seconds


if __name__ == '__main__':
    while True:
        tweet_crypto_assets()