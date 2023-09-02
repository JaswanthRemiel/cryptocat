
# CrptoCAT NFT

CryptoCat NFT" is a specialized Twitter bot with a paw firmly placed in the rapidly evolving world of Non-Fungible Tokens (NFTs). Renowned for its swift and comprehensive coverage of the NFT landscape, CryptoCat NFT relies on the power of the OpenSea API through Rapid API to efficiently source and share the latest NFT updates.

With an insatiable curiosity and a knack for real-time information, CryptoCat NFT scours NFT platforms, marketplaces, and communities to unearth the freshest content. Leveraging the OpenSea API's capabilities, it swiftly retrieves details about the most coveted NFT releases, highlights emerging NFT artists, tracks notable auction results, and follows trending NFT discussions.

Whether you're a seasoned NFT connoisseur or a newcomer to the realm of digital collectibles, CryptoCat NFT is your dedicated companion for staying informed about the vibrant NFT ecosystem. Thanks to its use of the OpenSea API via Rapid API, it delivers NFT updates with unparalleled speed and precision, ensuring you're always ahead of the curve in the world of Non-Fungible Tokens.










## Demo

![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHdwd2lzNGIwNWN3MXU3ZGl5MXBwdDRxbTE2a2RsYjVsZXR1cmZuMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nRPkdfRYhfNH4hq511/giphy.gif)
## API Call Reference
from tweepy
```bash
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


```
from Rapid-API
```bash
  import requests
  url = "https://opensea13.p.rapidapi.com/assets/"
  querystring = {"collection_slug":"cryptopunks","order_direction":"desc","limit":"20","include_orders":"false"}
  headers = {
	  "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	  "X-RapidAPI-Host": "opensea13.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers, params=querystring)
  print(response.json())
```


## Documentation

[Open sea API](https://rapidapi.com/Glavier/api/opensea13/)

[Tweepy](https://docs.tweepy.org/en/stable/)


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

